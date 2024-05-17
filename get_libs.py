def download_microdot():
    import mip

    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/src/microdot/microdot.py')
    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/src/microdot/utemplate.py')

    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/libs/common/utemplate/source.py')
    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/libs/common/utemplate/recompile.py')
    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/libs/common/utemplate/compiled.py')
    try:
        os.mkdir('lib/utemplate')
    except OSError:
        pass
    os.rename('lib/source.py','lib/utemplate/source.py')
    os.rename('lib/recompile.py','lib/utemplate/recompile.py')
    os.rename('lib/compiled.py','lib/utemplate/compiled.py')

    #soft reboot
    sys.exit()