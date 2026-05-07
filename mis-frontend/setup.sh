#!/bin/bash

echo "🚀 Setting up MIS Frontend"
echo "=========================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Installing Node.js 18..."

    # Install Node.js (you may need to run this with sudo)
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs

    echo "✅ Node.js installed successfully"
else
    echo "✅ Node.js is already installed"
fi

# Check if npm is available
if ! command -v npm &> /dev/null; then
    echo "❌ npm is not available. Please install Node.js first."
    exit 1
fi

echo "📦 Installing dependencies..."
npm install

echo "🎨 Setting up environment..."
if [ ! -f .env ]; then
    cat > .env << EOF
REACT_APP_API_URL=http://localhost:8001
EOF
    echo "✅ Created .env file"
fi

echo ""
echo "🎉 Frontend setup complete!"
echo ""
echo "To start the development server:"
echo "  npm start"
echo ""
echo "The app will be available at: http://localhost:3000"
echo ""
echo "Make sure the backend is running on port 8001 first:"
echo "  cd ../mis-backend"
echo "  PYTHONPATH=/home/oldman/MIS/mis-backend ./venv/bin/uvicorn mis-backend.main:app --host 0.0.0.0 --port 8001 --reload"