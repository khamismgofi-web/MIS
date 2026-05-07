import React, { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import api from '../api/api';
import {
  Plus,
  Search,
  MoreVertical,
  Edit,
  Trash2,
  CheckCircle,
  Circle,
  Calendar,
  User,
} from 'lucide-react';

const Tasks = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filter, setFilter] = useState('all'); // all, pending, completed
  const [showCreateModal, setShowCreateModal] = useState(false);
  const queryClient = useQueryClient();

  // Fetch tasks
  const { data: tasks, isLoading } = useQuery({
    queryKey: ['tasks'],
    queryFn: () => api.get('/api/v1/tasks/').then(res => res.data),
  });

  // Update task status mutation
  const updateTaskMutation = useMutation({
    mutationFn: ({ taskId, updates }) =>
      api.put(`/api/v1/tasks/${taskId}`, updates),
    onSuccess: () => {
      queryClient.invalidateQueries(['tasks']);
    },
  });

  // Delete task mutation
  const deleteTaskMutation = useMutation({
    mutationFn: (taskId) => api.delete(`/api/v1/tasks/${taskId}`),
    onSuccess: () => {
      queryClient.invalidateQueries(['tasks']);
    },
  });

  const filteredTasks = tasks?.filter(task => {
    const matchesSearch = task.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         task.description?.toLowerCase().includes(searchTerm.toLowerCase());

    const matchesFilter = filter === 'all' ||
                         (filter === 'pending' && !task.completed) ||
                         (filter === 'completed' && task.completed);

    return matchesSearch && matchesFilter;
  }) || [];

  const handleToggleComplete = (taskId, completed) => {
    updateTaskMutation.mutate({
      taskId,
      updates: { completed: !completed }
    });
  };

  const handleDeleteTask = (taskId) => {
    if (window.confirm('Are you sure you want to delete this task?')) {
      deleteTaskMutation.mutate(taskId);
    }
  };

  const getPriorityColor = (priority) => {
    switch (priority?.toLowerCase()) {
      case 'high':
        return 'bg-red-100 text-red-800';
      case 'medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'low':
        return 'bg-green-100 text-green-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-secondary-900">Tasks</h1>
          <p className="text-secondary-600">Track and manage your tasks.</p>
        </div>
        <button
          onClick={() => setShowCreateModal(true)}
          className="btn btn-primary flex items-center space-x-2"
        >
          <Plus className="h-4 w-4" />
          <span>New Task</span>
        </button>
      </div>

      {/* Search and Filter */}
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="relative flex-1">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Search className="h-5 w-5 text-secondary-400" />
          </div>
          <input
            type="text"
            placeholder="Search tasks..."
            className="input pl-10"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        <div className="flex space-x-2">
          {['all', 'pending', 'completed'].map((filterOption) => (
            <button
              key={filterOption}
              onClick={() => setFilter(filterOption)}
              className={`px-3 py-2 rounded-md text-sm font-medium capitalize ${
                filter === filterOption
                  ? 'bg-primary-100 text-primary-700'
                  : 'bg-secondary-100 text-secondary-600 hover:bg-secondary-200'
              }`}
            >
              {filterOption}
            </button>
          ))}
        </div>
      </div>

      {/* Tasks List */}
      <div className="space-y-4">
        {isLoading ? (
          [...Array(5)].map((_, i) => (
            <div key={i} className="card animate-pulse">
              <div className="flex items-center space-x-4">
                <div className="w-5 h-5 bg-secondary-200 rounded"></div>
                <div className="flex-1 space-y-2">
                  <div className="h-4 bg-secondary-200 rounded w-1/3"></div>
                  <div className="h-3 bg-secondary-200 rounded w-2/3"></div>
                </div>
              </div>
            </div>
          ))
        ) : (
          filteredTasks.map((task) => (
            <div key={task.id} className="card hover:shadow-md transition-shadow">
              <div className="flex items-start space-x-4">
                <button
                  onClick={() => handleToggleComplete(task.id, task.completed)}
                  className="mt-1"
                >
                  {task.completed ? (
                    <CheckCircle className="h-5 w-5 text-green-500" />
                  ) : (
                    <Circle className="h-5 w-5 text-secondary-400 hover:text-primary-500" />
                  )}
                </button>

                <div className="flex-1">
                  <div className="flex items-center justify-between">
                    <h3 className={`text-lg font-medium ${
                      task.completed ? 'text-secondary-500 line-through' : 'text-secondary-900'
                    }`}>
                      {task.title}
                    </h3>
                    <div className="flex items-center space-x-2">
                      <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${getPriorityColor(task.priority)}`}>
                        {task.priority || 'medium'}
                      </span>
                      <div className="relative">
                        <button className="p-1 rounded-full hover:bg-secondary-100">
                          <MoreVertical className="h-4 w-4 text-secondary-400" />
                        </button>
                      </div>
                    </div>
                  </div>

                  {task.description && (
                    <p className={`mt-1 text-sm ${
                      task.completed ? 'text-secondary-400' : 'text-secondary-600'
                    }`}>
                      {task.description}
                    </p>
                  )}

                  <div className="mt-3 flex items-center justify-between text-sm text-secondary-500">
                    <div className="flex items-center space-x-4">
                      {task.assigned_to && (
                        <div className="flex items-center space-x-1">
                          <User className="h-4 w-4" />
                          <span>{task.assigned_to}</span>
                        </div>
                      )}
                      {task.due_date && (
                        <div className="flex items-center space-x-1">
                          <Calendar className="h-4 w-4" />
                          <span>{new Date(task.due_date).toLocaleDateString()}</span>
                        </div>
                      )}
                    </div>

                    <button
                      onClick={() => handleDeleteTask(task.id)}
                      className="text-red-400 hover:text-red-600 p-1"
                    >
                      <Trash2 className="h-4 w-4" />
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))
        )}

        {filteredTasks.length === 0 && !isLoading && (
          <div className="text-center py-12">
            <CheckCircle className="mx-auto h-12 w-12 text-secondary-400" />
            <h3 className="mt-2 text-sm font-medium text-secondary-900">
              {filter === 'all' ? 'No tasks' : `No ${filter} tasks`}
            </h3>
            <p className="mt-1 text-sm text-secondary-500">
              {filter === 'all'
                ? 'Get started by creating a new task.'
                : `No tasks match the "${filter}" filter.`
              }
            </p>
          </div>
        )}
      </div>

      {/* Create Task Modal */}
      {showCreateModal && (
        <CreateTaskModal
          onClose={() => setShowCreateModal(false)}
          onSubmit={(taskData) => {
            // This would call the create task API
            console.log('Create task:', taskData);
            setShowCreateModal(false);
          }}
          loading={false}
        />
      )}
    </div>
  );
};

// Create Task Modal Component
const CreateTaskModal = ({ onClose, onSubmit, loading }) => {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    priority: 'medium',
    due_date: '',
    assigned_to: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-lg max-w-md w-full p-6">
        <h2 className="text-lg font-semibold text-secondary-900 mb-4">
          Create New Task
        </h2>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="title" className="label">
              Task Title
            </label>
            <input
              type="text"
              id="title"
              name="title"
              required
              className="input"
              placeholder="Enter task title"
              value={formData.title}
              onChange={handleChange}
            />
          </div>

          <div>
            <label htmlFor="description" className="label">
              Description
            </label>
            <textarea
              id="description"
              name="description"
              rows={3}
              className="input"
              placeholder="Enter task description"
              value={formData.description}
              onChange={handleChange}
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label htmlFor="priority" className="label">
                Priority
              </label>
              <select
                id="priority"
                name="priority"
                className="input"
                value={formData.priority}
                onChange={handleChange}
              >
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
              </select>
            </div>

            <div>
              <label htmlFor="due_date" className="label">
                Due Date
              </label>
              <input
                type="date"
                id="due_date"
                name="due_date"
                className="input"
                value={formData.due_date}
                onChange={handleChange}
              />
            </div>
          </div>

          <div>
            <label htmlFor="assigned_to" className="label">
              Assign To
            </label>
            <input
              type="text"
              id="assigned_to"
              name="assigned_to"
              className="input"
              placeholder="Enter assignee name"
              value={formData.assigned_to}
              onChange={handleChange}
            />
          </div>

          <div className="flex space-x-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="flex-1 btn btn-secondary"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={loading}
              className="flex-1 btn btn-primary disabled:opacity-50"
            >
              {loading ? 'Creating...' : 'Create Task'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Tasks;