# MIS Platform Frontend

A modern React frontend for the Management Information System (MIS) Platform.

## Features

- **Dashboard**: Overview of system statistics and recent activities
- **Projects Management**: Create, view, and manage projects
- **User Management**: Admin interface for managing users
- **Task Management**: Track and manage tasks with priorities
- **Authentication**: JWT-based login and registration
- **Responsive Design**: Mobile-friendly interface with Tailwind CSS
- **Real-time Updates**: Using React Query for efficient data fetching

## Tech Stack

- **React 18**: Modern React with hooks
- **React Router**: Client-side routing
- **TanStack Query**: Data fetching and caching
- **Tailwind CSS**: Utility-first CSS framework
- **Axios**: HTTP client for API calls
- **Lucide React**: Beautiful icons
- **Headless UI**: Accessible UI components

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Running MIS Backend server

### Installation

1. Navigate to the frontend directory:
   ```bash
   cd mis-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The application will open at `http://localhost:3000`

### Environment Variables

Create a `.env` file in the frontend root:

```env
REACT_APP_API_URL=http://localhost:8001
```

## Project Structure

```
src/
├── api/           # API service functions
├── components/    # Reusable UI components
├── hooks/         # Custom React hooks
├── pages/         # Page components
├── App.js         # Main app component
├── index.js       # App entry point
└── index.css      # Global styles
```

## Available Scripts

- `npm start`: Start development server
- `npm build`: Build for production
- `npm test`: Run tests
- `npm eject`: Eject from Create React App

## API Integration

The frontend communicates with the FastAPI backend through REST endpoints:

- Authentication: `/api/v1/auth/`
- Users: `/api/v1/users/`
- Projects: `/api/v1/projects/`
- Tasks: `/api/v1/tasks/`

## Features Overview

### Dashboard
- System statistics (users, projects, tasks)
- Recent activities feed
- Quick action buttons

### Projects
- List all projects with search
- Create new projects
- View project details
- Edit and delete projects

### Users
- User management interface
- Role-based access control
- User creation and management

### Tasks
- Task creation and management
- Priority levels (low, medium, high)
- Due dates and assignments
- Status tracking (pending/completed)

### Authentication
- JWT token-based authentication
- Login/logout functionality
- Protected routes
- Automatic token refresh

## Styling

The application uses Tailwind CSS for styling with custom utility classes defined in `index.css`. The design follows a clean, modern aesthetic with:

- Primary color: Blue (#3B82F6)
- Secondary colors: Gray variations
- Consistent spacing and typography
- Responsive grid layouts
- Hover states and transitions

## Contributing

1. Follow the existing code style
2. Use meaningful component and variable names
3. Add proper error handling
4. Test your changes
5. Update documentation as needed

## License

This project is part of the MIS Platform.