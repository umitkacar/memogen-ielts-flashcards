#!/bin/bash
echo "🚀 Starting local test server..."
echo "📂 Files in current directory:"
ls -la index.html .nojekyll README.md 2>/dev/null
echo ""
echo "✅ Open your browser and visit:"
echo "   http://localhost:8000"
echo ""
echo "🔍 Testing if index.html works..."
if [ -f "index.html" ]; then
    echo "✅ index.html found!"
    head -20 index.html | grep -i "MEMOGEN"
else
    echo "❌ index.html NOT found!"
fi
