def initialSetup():
    from pkg_resources import WorkingSet, DistributionNotFound
    workingSet = WorkingSet()
    requirements = ['psutil']
    print 'Checking dependencies......'
    for requirement in requirements:
        try:
            dep = workingSet.require(requirement)
            print 'Dependency found....'
            print 'Countinuing to the program...'
        except DistributionNotFound:
            print 'Installing dependencies...'
            from setuptools.command.easy_install import main as install
            try:
                install([requirement])
                print 'Dependency installed...'
                print 'Continuing....'
            except Exception:
                print 'Coudn\'t install dependencies...'