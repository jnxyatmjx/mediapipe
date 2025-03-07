## mediapipe
### compile gstreamer static
```shell
  -I/home/cerbero/build/dist/linux_x86_64/include/gstreamer-1.0 -I/home/cerbero/build/dist/linux_x86_64/include/orc-0.4 -I/home/cerbero/build/dist/linux_x86_64/include/gstreamer-1.0 -I/home/cerbero/build/dist/linux_x86_64/include/gio-unix-2.0 -I/home/cerbero/build/dist/linux_x86_64/include/gstreamer-1.0 -I/home/cerbero/build/dist/linux_x86_64/include/glib-2.0 -I/home/cerbero/build/dist/linux_x86_64/lib/glib-2.0/include -L/home/cerbero/build/dist/linux_x86_64/lib -Wl,-Bstatic -lgstrtspserver-1.0 -lgstrtsp-1.0 -lgstsdp-1.0 -lgstrtp-1.0 -lgstaudio-1.0 -lgsttag-1.0 -lorc-0.4 -lgstnet-1.0 -lgio-2.0 -lresolv -lz -lgstapp-1.0 -lgstbase-1.0 -lgstreamer-1.0 -Wl,--export-dynamic -lgmodule-2.0 -lunwind -llzma -lgobject-2.0 -lffi -lglib-2.0 -Wl,-Bdynamic -lm -ldl -pthread
```
or 
```shell
-I/home/cerbero/build/dist/linux_x86_64/include/gstreamer-1.0 -I/home/cerbero/build/dist/linux_x86_64/include/orc-0.4 -I/home/cerbero/build/dist/linux_x86_64/include/gstreamer-1.0 -I/home/cerbero/build/dist/linux_x86_64/include/gio-unix-2.0 -I/home/cerbero/build/dist/linux_x86_64/include/gstreamer-1.0 -I/home/cerbero/build/dist/linux_x86_64/include/glib-2.0 -I/home/cerbero/build/dist/linux_x86_64/lib/glib-2.0/include -L/home/cerbero/build/dist/linux_x86_64/lib -Wl,-Bstatic -lgstrtspserver-1.0 -lgstrtsp-1.0 -lgstsdp-1.0 -lgstrtp-1.0 -lgstaudio-1.0 -lgsttag-1.0 -lorc-0.4 -lgstnet-1.0 -lgio-2.0 -lresolv -lz -lgstapp-1.0 -lgstbase-1.0 -lgstreamer-1.0 -lgmodule-2.0 -lunwind -llzma -lgobject-2.0 -lffi -lglib-2.0 -Wl,-Bdynamic -lm -ldl -pthread
```
