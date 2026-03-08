#!/bin/bash

# 构建 frontend_main
echo "=== build funchat frontend main ==="
cd frontend_main
pnpm install
if [ $? -ne 0 ]; then
    echo "frontend_main install error"
    exit 1
fi
pnpm build
if [ $? -ne 0 ]; then
    echo "frontend_main build error"
    exit 1
fi
cd ..

# 构建 frontend_window
echo ""
echo "=== build frontend_window ==="
cd frontend_window
pnpm install
if [ $? -ne 0 ]; then
    echo "frontend_window install error"
    exit 1
fi
pnpm build
if [ $? -ne 0 ]; then
    echo "frontend_window build error"
    exit 1
fi
cd ..

# 构建 backend
echo ""
echo "=== build backend ==="
cd backend
pnpm install
if [ $? -ne 0 ]; then
    echo "backend install error"
    exit 1
fi
pnpm build
if [ $? -ne 0 ]; then
    echo "backend build error"
    exit 1
fi
cd ..

# 运行 Python 脚本移动文件
echo ""
echo "=== run Python : moveDist.py ==="
python moveDist.py
