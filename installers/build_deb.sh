#!/bin/bash
set -e

APP_NAME="sentinelops"
VERSION="1.0"
ARCH="all"
BUILD_DIR="build/${APP_NAME}_${VERSION}"
mkdir -p "${BUILD_DIR}/DEBIAN"
mkdir -p "${BUILD_DIR}/usr/local/bin"

# Create control file
cat <<EOF > "${BUILD_DIR}/DEBIAN/control"
Package: ${APP_NAME}
Version: ${VERSION}
Section: base
Priority: optional
Architecture: ${ARCH}
Depends: python3, python3-pip
Maintainer: rfc391 <robshubert96@gmail.com>
Description: SentinelOps Tactical Intelligence Framework
EOF

# Copy main app entry point
cp ../../src/main.py "${BUILD_DIR}/usr/local/bin/${APP_NAME}"
chmod +x "${BUILD_DIR}/usr/local/bin/${APP_NAME}"

# Build package
dpkg-deb --build "${BUILD_DIR}"
echo "Built ${APP_NAME}_${VERSION}.deb in build/"
