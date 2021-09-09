Autosave
--------

This application was created via
```
makeBaseApp.pl -t ioc autosave
makeBaseApp.pl -t ioc -i autosave
```

Next this section was added to `autosaveApp/src/Makefile`:
```
autosave_DBD += asSupport.dbd
autosave_LIBS += autosave
```

An example database was added to the `Db` folder and added to the associated `Makefile`,
and an example display in the `opi` folder.

Finally, `iocBoot/ioc_autosave/st.cmd` was prepared with example autosave configuration commands,
which where then commented out.
