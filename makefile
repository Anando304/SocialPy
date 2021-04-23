PY = python3
COVERAGE = coverage
UNITTEST = unittest
PYFLAGS = --cov-report html --cov=src/ 
DOXY = doxygen
DOXYCFG = doxConfig

RMDIR = rm -rf

.PHONY: run test doc clean

run:
	$(PY) src/"Social Media App"/main.py
	
test:
	cd src/"Social Media App" && $(PY) -m $(UNITTEST) UnitTests/TestRunner.py
	
test_coverage:
	# ONLY FOR WINDOWS PyCharm TERMINAL. RUNNING ON LINUX WILL READ RANDOM .PYC FILES SO DO NOT RUN FOR LINUX
	#cd src/"Social Media App" && $(COVERAGE) run --branch -m $(UNITTEST) discover -s UnitTests -vv && $(COVERAGE) report -m && $(COVERAGE) html
	
	# WORKS FOR BOTH LINUX,MAC,WINDOWS WITHOUT READING RANDOM .PYC FILES
	#cd src/"Social Media App" && $(COVERAGE) run --branch --source=./UnitTests/General -m $(UNITTEST) discover -s UnitTests/General && coverage report -m
	#cd src/"Social Media App" && $(COVERAGE) run --branch --source=./UnitTests/Function_NonFunc_UnitTests -m $(UNITTEST) discover -s UnitTests/Function_NonFunc_UnitTests && coverage report
	cd src/"Social Media App" && $(COVERAGE) run --branch --source=./UnitTests/ -m $(UNITTEST) discover -s UnitTests -vv && $(COVERAGE) report -m && $(COVERAGE) html

doc:
	$(DOXY) $(DOXYCFG)
	cd Doc/Design/MIS/latex && $(MAKE)

clean:
	@- $(RMDIR) cd Doc/Design/MIS/html
	@- $(RMDIR) cd Doc/Design/MIS/htmlcov
	@- $(RMDIR) cd Doc/Design/MIS/latex
