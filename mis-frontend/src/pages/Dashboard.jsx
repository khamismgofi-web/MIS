import React from 'react';
import { useQuery } from '@tanstack/react-query';
import api from '../api/api';
import {
  Users,
  FolderOpen,
  CheckSquare,
  TrendingUp,
  Activity,
  Calendar,
} from 'lucide-react';

const Dashboard = () => {
  // Fetch dashboard statistics
  const { data: stats, isLoading: statsLoading } = useQuery({
    queryKey: ['dashboard-stats'],
    queryFn: async () => {
      const [usersRes, projectsRes, tasksRes] = await Promise.all([
        api.get('/api/v1/users/'),
        api.get('/api/v1/projects/'),
        api.get('/api/v1/tasks/'),
      ]);

      return {
        users: usersRes.data.length,
        projects: projectsRes.data.length,
        tasks: tasksRes.data.length,
      };
    },
  });

  // Fetch recent activities
  const { data: activities, isLoading: activitiesLoading } = useQuery({
    queryKey: ['recent-activities'],
    queryFn: async () => {
      // This would be a real endpoint in a full implementation
      return [
        {
          id: 1,
          type: 'project_created',
          message: 'New project "Website Redesign" was created',
          timestamp: new Date(Date.now() - 1000 * 60 * 30), // 30 minutes ago
        },
        {
          id: 2,
          type: 'user_joined',
          message: 'John Doe joined the platform',
          timestamp: new Date(Date.now() - 1000 * 60 * 60 * 2), // 2 hours ago
        },
        {
          id: 3,
          type: 'task_completed',
          message: 'Task "Setup CI/CD pipeline" was completed',
          timestamp: new Date(Date.now() - 1000 * 60 * 60 * 4), // 4 hours ago
        },
      ];
    },
  });

  const StatCard = ({ title, value, icon: Icon, color, trend, borderColorHex }) => (
    <div className="card border-b-4" style={{borderBottomColor:borderColorHex}}>
      <div className="flex items-center">
        <div className={`p-3 rounded-full ${color}`}>
          <Icon className="h-6 w-6 text-white" />
        </div>
        <div className="ml-4">
          <p className="text-sm font-medium text-secondary-600">{title}</p>
          <p className="text-2xl font-bold text-secondary-900">
            {statsLoading ? '...' : value}
          </p>
          <p className="text-xs text-green-500 mt-2">{trend} 
          </p>
        </div>
      </div>
    </div>
  );

  const formatTimeAgo = (date) => {
    const now = new Date();
    const diffInMinutes = Math.floor((now - date) / (1000 * 60));

    if (diffInMinutes < 60) {
      return `${diffInMinutes}m ago`;
    } else if (diffInMinutes < 1440) {
      return `${Math.floor(diffInMinutes / 60)}h ago`;
    } else {
      return `${Math.floor(diffInMinutes / 1440)}d ago`;
    }
  };

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-secondary-900">Dashboard</h1>
        <p className="text-secondary-600">Welcome back! Here's what's happening.</p>
      </div>

      {/* Statistics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <StatCard
          title="Total Users"
          value={stats?.users || 0}
          icon={Users}
          color="bg-blue-500"
          trend="⤒ 12% from last month"
          borderColorHex="#3b82f6"
        />
        <StatCard
          title="Active Projects"
          value={stats?.projects || 0}
          icon={FolderOpen}
          color="bg-green-500"
          trend="⤒ 3 new this week"
          borderColorHex="#22c55e"
        />
        <StatCard
          title="Tasks Completed"
          value={stats?.tasks || 0}
          icon={CheckSquare}
          color="bg-purple-500"
          trend="⤒ 8 completed today"
          borderColorHex="#a855f7"
        />
      </div>

      {/* Recent Activities */}
      <div className="card">
        <div className="flex items-center mb-4">
          <Activity className="h-5 w-5 text-secondary-600 mr-2" />
          <h2 className="text-lg font-semibold text-secondary-900">
            Recent Activities
          </h2>
        </div>

        {activitiesLoading ? (
          <div className="space-y-3">
            {[...Array(3)].map((_, i) => (
              <div key={i} className="animate-pulse">
                <div className="h-4 bg-secondary-200 rounded w-3/4 mb-2"></div>
                <div className="h-3 bg-secondary-200 rounded w-1/4"></div>
              </div>
            ))}
          </div>
        ) : (
          <div className="space-y-4">
            {activities?.map((activity) => (
              <div key={activity.id} className="flex items-start space-x-3">
                <div className="flex-shrink-0">
                  <div className="w-2 h-2 bg-primary-500 rounded-full mt-2"></div>
                </div>
                <div className="flex-1">
                  <p className="text-sm text-secondary-900">{activity.message}</p>
                  <p className="text-xs text-secondary-500 flex items-center mt-1">
                    <Calendar className="h-3 w-3 mr-1" />
                    {formatTimeAgo(activity.timestamp)}
                  </p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Quick Actions */}
      <div className="card">
        <h2 className="text-lg font-semibold text-secondary-900 mb-4">
          Quick Actions
        </h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <button className="btn btn-primary w-full">
            Create New Project
          </button>
          <button className="btn btn-secondary w-full">
            Add New User
          </button>
          <button className="btn btn-secondary w-full">
            View Reports
          </button>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
