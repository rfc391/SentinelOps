#!/bin/bash
set -e

APP=SentinelOps
VERSION=1.0
APPDIR=${APP}.AppDir

# Setup structure
mkdir -p ${APPDIR}/usr/bin
cp ../../src/main.py ${APPDIR}/usr/bin/${APP}
chmod +x ${APPDIR}/usr/bin/${APP}

# Create AppRun
cat <<EOF > ${APPDIR}/AppRun
#!/bin/bash
exec \$APPDIR/usr/bin/${APP} "\$@"
EOF
chmod +x ${APPDIR}/AppRun

# Create desktop entry
cat <<EOF > ${APPDIR}/${APP}.desktop
[Desktop Entry]
Name=${APP}
Exec=${APP}
Icon=utilities-terminal
Type=Application
Categories=Utility;
EOF

# Download AppImageTool if needed
if [ ! -f appimagetool ]; then
  wget https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage -O appimagetool
  chmod +x appimagetool
fi

# Build AppImage
./appimagetool ${APPDIR} ${APP}-${VERSION}.AppImage
echo "AppImage created: ${APP}-${VERSION}.AppImage"
