Documentation for Program MNDO99.
Version 6.1 of 12 April 2003 

--- needs to be upgraded ---
--- does not reflect the current status of the code ---

By Walter Thiel, Max-Planck-Institut fuer Kohlenforschung,
Kaiser-Wilhelm-Platz 1, D-45470 Muelheim, Germany.


------------------------------------------------------------------------


Contents.

1.    Introduction.

2.    Summary of options.
2.1.  Available semiempirical methods.
2.2.  Available types of wavefunctions.
2.3.  Available types of calculations.
2.4.  Available analytic derivatives.
2.5.  Available properties.

3.    Installation and validation.
3.1.  General information.
3.2.  Installation procedure.
3.3.  Validation procedure.
3.4.  Standard test jobs.
3.5.  MOPAC test jobs.
3.6.  Possible modifications.
3.7.  Special information for Cray.
3.8.  Special information on files.

4.    Program size and memory allocation.
4.1.  General comments.
4.2.  Use of blank common: Geometry optimization and SCF calculation.
4.3.  Use of blank common: Second-order perturbation treatment.
4.4.  Use of blank common: Other tasks.

5.    Comments on input options.
5.1.  Available modes of input.
5.2.  Cartesian vs. internal coordinates.
5.3.  Symmetry conditions.
5.4.  Automatic detection of symmetry.
5.5.  Geometry optimizations.
5.6.  Restarts.
5.7.  Diagonalization routines.
5.8.  SCF convergence criteria.

6.    References.

Appendices.

A.    Parameters.
B.    Limitations of the program.


------------------------------------------------------------------------


## 1. Introduction.

This documentation is intended to
- give a summary of the available options,
- guide the installation and validation of the program,
- discuss technical issues such as memory management, and
- provide some background information on certain input options.

The user is referred to the following sources for more detail:
- Original papers (see references in section 6 and appendix A).
- Detailed input description (see file mndo99.txt).

Theory and applications of semiempirical quantum-chemical methods
are not covered here since they have been reviewed elsewhere [1-3].



## 2. Summary of options.

2.1.  Available semiempirical methods.

The following methods are implemented (see input variable iop).
- MNDO [4], iop=0.
Parameters are included for the elements
H,He,Li,Be,B,C,N,O,F,Mg,Al,Si,P,S,Cl,Zn,Ge,Br,Sn,I,Hg,Pb.
- MNDOC [5], iop=-1.
Parameters are included for H,C,N,O.
- MNDO/d [6,7], iop=-10.
Parameters for H,He,Li,Be,B,C,N,O,F are the same as in MNDO.
MNDO/d parameters are included for Na,Mg,Al,Si,P,S,Cl,Ti,Fe,Ni,
Cu,Zn,Ga,Ge,As,Se,Br,Zr,Pd,Ag,Cd,In,Sn,Sb,Te,I,Hf,Hg,Tl.
Those for Na,Mg,Al,Si,P,S,Cl,Br,I,Zn,Cd,Hg are final [7].
Those for other elements are preliminary until published.
- AM1 [8], iop=-2.
Parameters for H,B,C,N,O,F,Al,Si,P,S,Cl,Zn,Ge,Br,Sn,I,Hg.
- PM3 [9], iop=-7.
Parameters for H,Be,C,N,O,F,Mg,Al,Si,P,S,Cl,Zn,Ga,Ge,As,Se,Br,
Cd,In,Sn,Sb,Te,I,Hg,Tl,Pb,Bi.
- OM1 [10], iop=-5.
Parameters for H,C,N,O,F.
- OM2 [11], iop=-6.
Parameters for H,C,N,O.
- MINDO/3 [12], iop=1.
Parameters for H,B,C,N,O,F,Si,P,S,Cl.
- CNDO/2 [13], iop=2.
Parameters for H,Li,Be,B,C,N,O,F.
- SCC-DFTB for C,H,N,O [Elstner et al., Phys. Rev. B, 58:7260-7268 (1998)]
Appendix A lists the literature references for all parameters that
are included in the program.

The following special variants of MNDO are provided.
- MNDO/H [14], iop=-3.
Special treatment of hydrogen bonds.
Hydrogen bonds X...H-Y are automatically identified by the
program using the following criteria.
a) Atoms X and Y must be nitrogen, oxygen, or fluorine.
b) The distance X...H must be in the range rhxmin...rhxmax.
c) The distance H-Y must be the shortest distance involving H.
d) The angle X...H-Y must be greater than angmin.
The default criteria (rhxmin=1.1 angstrom, rhxmax=5.0 angstrom,
angmin=90 degree) may be changed using input option ihbond.
If all criteria above are satisfied, the program applies the
modified core-core repulsion function for X...H [14].
It is the responsibility of the user to check the geometry
and make sure that these criteria identify all hydrogen bonds
in the system under study.
- MNDO/dH, iop=-13.
Special treatment of hydrogen bonds.
Completely analogous to MNDO/H (see above), except that
second-row and heavier elements are treated by MNDO/d.
- MNDO with original parameters for Si and S (appendix A.10).
Accessible via iop=-4 in combination with iparok=4.
Recommendation: Use the default MNDO parameters.
- MNDO with dependent parameters copied from MNDO87-MNDO89.
Accessible via iop=-4 in combination with iparok=5.
Recommendation: Use the slightly less precise default values
which are identical with those used in program MOPAC(6.0).
The numerical deviations are negligible in practice.
- MNDO with special parameters for fullerenes (appendix A.10).
Accessible via iop=-4 in combination with iparok=6.
Comment: Possibly of interest in fullerene studies.
The last three variants (iop=-4, iparok=4-6) are rarely used.

2.2.  Available types of wavefunctions.

The following SCF treatments are implemented.
- Closed-shell restricted Hartree-Fock (RHF) [15].
Chosen by default for closed-shell systems (imult=0).
- Open-shell unrestricted Hartree-Fock (UHF) [16].
Chosen for open-shell systems (imult>0) by option iuhf=1.
This is default when using standard input (see section 5.1).
- Half-electron RHF [17].
Chosen for open-shell systems (imult=1,2,3) by option iuhf=-1.
This is default when using MOPAC input (see section 5.1).
- UHF for singlets.
Chosen for singlets (imult=0) by option iuhf=1.
This will normally lead to the closed-shell RHF solution
unless there are SCF instabilities.


The following correlation treatments are implemented.
- Minimal configuration interaction for singlets and doublets.
a) 3*3 or 2*2 CI for singlets using closed-shell MOs (imult=0).
b) 3*3 CI for singlets using half-electron RHF MOs (imult=1).
c) 2*2 CI for doublets using half-electron RHF MOs (imult=2).
- Second-order perturbation treatment for singlets based on
closed-shell RHF MOs (imult=0). Rayleigh-Schroedinger (RS)
and Brillouin-Wigner (BW) perturbation approaches may be used
in conjunction with Moller-Plesset (MP) and Epstein-Nesbet (EN)
energy denominators, the default being BWEN. The reference
wavefunction is either a closed-shell RHF determinant (kci=2)
or a 2*2 CI wavefunction (kci=3,4). For methodological details
the user should consult ref.[5].

It is strongly recommended that applications are done with an
established combination of SCF and correlation treatments. To
be specific, all semiempirical methods except MNDOC will
normally be applied at the SCF level (without correlation)
unless unusual bonding situations require the use of a minimal
CI treatment. MNDOC geometry optimizations can normally be
carried out at the SCF level, whereas energy evaluations are
done at the MNDOC BWEN level [5,18].

2.3.  Available types of calculation.

The following types of calculation are possible depending on
the input variable jop.
- Gradient calculation at the fixed input geometry   , jop=-2.
- Standard calculation at the fixed input geometry   , jop=-1.
- Geometry optimization for energy minimum           , jop= 0.
- Geometry optimization for transition state         , jop= 1.
- Force constant analysis at the fixed input geometry, jop= 2.
- Geometry optimization for input geometry followed
by force constant analysis at optimized geometry   , jop= 3.
- Geometry optimization for transition state followed
by force constant analysis at optimized geometry   , jop= 4.
- Choice between jop=2 and jop=3, with a geometry
optimization only in the case of a large gradient  , jop= 5.
- Choice between jop=2 and jop=4, with a geometry
optimization only in the case of a large gradient  , jop= 6.
Options jop=5,6 are included for MOPAC compatibility.

Several techniques for geometry optimization may be employed
including quasi-Newton energy minimizations (e.g. BFGS or DFP),
gradient norm minimization, and eigenvector following (EF).

Harmonic force constants can be calculated either analytically
or by numerical differentiation of the gradient. A subsequent
normal coordinate treatment characterizes stationary points
and provides harmonic frequencies as well as other vibrational
properties. Isotopic substitution is possible (option kmass).

Reaction path calculations (option kgeom=1) and two-dimensional
grid calculations (option kgeom=2) can be carried out for jop
values between -2 and 1 (see above). Paths and grids can be
defined in a very simple manner (see file mndo99.txt).

2.4.  Available analytic derivatives

Analytic first derivatives of the energy with respect to nuclear
coordinates are implemented for MNDO-type methods (MNDO, AM1, PM3,
MNDO/d) and the following types of wavefunctions [19,20]:
- Closed-shell RHF,
- open-shell UHF,
- open-shell half-electron,
- minimal configuration interaction.
In the latter two cases, the computation times for evaluating
the gradient in large molecules are orders of magnitude smaller
than in previous analytic or numerical approaches (for details,
see [19,20]). This is due to the fact that the computational
effort scales as N**3 (for the solution of the coupled perturbed
Hartree-Fock equations via the Z-vector algorithm) compared with
N**4 previously (N electrons).

Analytic second derivatives of the energy with respect to nuclear
coordinates are implemented for MNDO-type methods (MNDO, AM1, PM3,
MNDO/d) and variational wavefunctions [21]:
- Closed-shell RHF,
- open-shell UHF.
Computation times are typically reduced by a factor of 5 relative
to the numerical differentiation of gradients.

Analytic derivatives are selected by default (when appropriate).

2.5.  Available properties.

Each calculation provides the energy of the system studied.
Following the usual semiempirical conventions, the total energy
is expressed as heat of formation at 298 K.

Geometry optimizations yield equilibrium structures at stationary
points (minima, trasition states, or higher-order saddle points)
and the corresponding equilibrium rotational constants.

Force constant computations give harmonic vibrational frequencies,
the associated normal modes, zero-point vibrational energies,
and infrared intensities. Using statistical thermodynamics,
several thermodynamic properties are provided as a function of
temperature (including enthalpies, entropies, free enthalpies,
and heat capacities). The heat of formation at 0 K is also
determined.

The energies of the occupied molecular orbitals approximate
the corresponding vertical ionization potentials quite well
(Koopmans' theorem). Energies of singly excited configurations
can be computed as a rough estimate of the energy of singly
excited states (singlets or triplets).

Population analysis of the molecular orbital wavefunctions
yields orbital populations and net atomic charges indicating
the electronic charge distribution in the molecule.

Dipole moments are evaluated as expectation values using the
standard semiempirical integral approximations.

Static electric properties, i.e. polarizabilities (alpha) and
hyperpolarizabilities (beta, gamma), can be calculated using a
finite-field perturbation technique (options ifld1, ifld2, and
ifld3).

Electrostatic potentials and electric fields can be calculated
at external points (option mminp). The electrostatic interactions
may be treated classically (Coulomb interactions between point
charges, optionally including point dipoles and quadrupoles)
or semiempirically [22,23].

NMR chemical shifts can be computed for MNDO-type methods [24]
(option nmr). It is recommended to use special parametrizations
for NMR chemical shifts (MNDO-B preferred over MNDO-A; parameters
available for H,C,N,O). Calculations without three-center terms
are appropriate for C,N,O. Three-center terms should be included
for H and NICS (even though such computations are costly).

Solvation effects can be taken into account by the COSMO approach
(option icosmo). Cavitation and dispersion contributions may be
evaluated by a parametric treatment [25] when water is used as
solvent (for MNDO and AM1 only).



## 3. Installation and validation.

### 3.1. General information.

The software is provided either as a tar file (mndo99u.tar) or as
a gzipped tar file (mndo99u.tar.gzip). These files are processed
by the following Unix commands:

gunzip mndo99u.tar.gzip
tar -xf mndo99u.tar

The first command is needed to convert the gzipped tar file
mndo99u.tar.gzip (if delivered as such) into a regular tar file
(mndo99u.tar). The second command generates a directory mndo99u
with some subdirectories (99,BLAS,LAPACK,PS,testjobs,testmopac6,
testps).

Contents of the directories (brief summary):

mndo99u
READ_ME      General overview
Makefile     Makefile for installing MNDO99
*.mak        Machine-specific definitions for Makefile
MNDO99.f     Main program for MNDO99
mndo99.doc   This documentation
mndo99.txt   Input description
mndogrepall  Script for testing
testall      Script for testing
99/          General MNDO99 source code
BLAS/        Source code for BLAS routines
LAPACK/      Source code for LAPACK routines
PS/          Source code for analytic derivatives and NMR
testanu/     Benchmark suite from ANU
testjobs/    Standard MNDO99 test jobs
testmopac6/  Test jobs from MOPAC(6.0)
testps/      Test jobs for analytic derivatives and NMR

99/
*.f          MNDO99 routines
Makefile     Makefile for compilation and creation of library
memx.c       C routines for memory management under UNICOS

BLAS/
*.f          BLAS routines
Makefile     Makefile for compilation and creation of library
READ_ME      Source of routines

LAPACK/
*.f          LAPACK routines
Makefile     Makefile for compilation and creation of library
READ_ME      Source of routines

PS/
*.f          Routines for analytic derivatives and NMR
Makefile     Makefile for compilation and creation of library

testanu/
*.inp        14 benchmark jobs from ANU
testanugo    Script for running these jobs
anu.grep     Reference summary of results
READ_ME      Information on benchmark jobs

testjobs/
*.inp        50 standard MNDO99 test jobs
testjobsgo   Script for running these jobs
jobs.ref     Reference output
jobs.grep    Reference summary of results
READ_ME      Information on test jobs

testmopac6/
*.inp        8 standard MOPAC(6.0) test jobs
testmopac6go Script for running these jobs
mopacs.grep  Reference summary of results
READ_ME      Information on test jobs

testps/
*.inp        14 analytic derivative test jobs
*.opt        Reference results for the test jobs
Makefile     Makefile to run and evaluate the test jobs
check.awk    File used by awk to check the results
awk.out      Reference output by awk for correct results
READ_ME      Information on test jobs

### 3.2. Installation procedure.

The top directory mndo99u provides a Makefile which controls the installation of MNDO99. 
Makefile contains a command include machine.mak to account for any machine-specific settings. 
Assuming that this file machine.mak exists, MNDO99 is installed by a single command issued from the working directory mndo99u: make The executable program is named mndo.

The following sample files *.mak are available in mndo99u:

aix3.mak      for IBM/RS6000 under AIX(3.2.4),  
aix4.mak      for IBM/RS6000 under AIX(4.2.1),  
irix5.mak     for SGI-R4000/R5000  under IRIX(5.x),  
irix6.mak     for SGI-R8000/R10000 under IRIX(6.x),  
osf1.mak      for DEC Alpha under OSF/1.  

It is recommended to make a symbolic link from machine.mak to any such specific *.mak file. 
For example, MNDO99 is installed on SGI-R10000 workstations as follows:
ln -s irix6.mak machine.mak
make

In addition, a template (standard.mak) is provided as a starting
point for installations on other UNIX machines. After suitable
modification of this template, MNDO99 can be installed by the
following two commands:
ln -s standard.mak machine.mak
make
Inspection of Makefile and standard.mak shows that optimization
by the f77 compiler is restricted to the -O1 level and that the
standard Fortran versions of the BLAS routines are used in the
template.

Performance may be improved by choosing a higher optimization
level and particularly by employing optimized versions of the
BLAS routines. This can be achieved through machine-specific
*.mak files (see the examples included).

If a specific *.mak file is not provided here for a given target
machine, it is recommended to generate such a file whenever
large-scale applications are intended. The comments in Makefile
and in the available *.mak sample files should offer sufficient
guidance in this endeavour. It is particularly important for
optimum performance to have efficient BLAS routines, e.g. from
the corresponding machine libraries.

### 3.3. Validation procedure.

There are three subdirectories (testjobs, testmopac6, testps)
with test inputs and test outputs which are used for validation.
The top directory mndo99u provides a script (testall) which
carries out the test jobs in these subdirectories. The command
testall
will generate an output file (testall.out) which can be checked
for a quick validation. To understand the contents of this file,
the procedures applied in the subdirectories (testjobs, testmopac6,
testps) are outlined in the following.

Procedure in subdirectory testjobs:
Execution of the script testjobsgo will carry out all test jobs
in this subdirectory (*.inp) and generate the corresponding
outputs (*.out) as well as a summary output file (all.grep).
These may be compared against the available reference outputs
(jobs.ref, produced by cat *.out > jobs.ref) and the reference
summary (jobs.grep). The latter comparison is done automatically
in testjobsgo by using the UNIX command
diff jobs.grep all.grep > x
so that inspection of the temporary file x will allow immediate
verification of a correct installation. When invoked from script
../testall, file x is appended to file ../testall.out.

Procedure in subdirectory testmopac6:
Completely analogous, except for different files names (script
testmopac6go, reference output mopac6.ref, reference summary
file mopac6.grep).

Procedure in subdirectory testps:
A Makefile is provided for automatic testing, in combination with
check.awk. The command
make
runs all test jobs using the input files provided (*.inp), compares
the corresponding outputs (*.out) against the reference results
(*.opt) and produces diagnostic files (*.pass or *.fail) along with
the appropriate messages. A successful installation is shown by the
absence of *.fail files. The script ../testall employs the commands
make clean
make >& xou
cat xou >> ../testall.out
in order to delete previous *.pass files, to perform the tests,
and to append the diagnostic messages to file ../testall.out.

Common remarks for all tests:
- For identical program versions and the same type of host machine
the *.grep files from the installed program should be identical
to those provided as a reference, except for the computation
times printed, of course.
- For different program versions or for different types of host
machines, slightly different results may be tolerated. Such
differences can arise from different algorithms in different
program versions, e.g. for the formation of the Fock matrix
of large molecules which may be handled differently on vector
machines and on scalar machines (see below).
- Any such differences should not exceed:
0.0001 kcal/mol      for heats of formation,
0.01   kcal/(mol*A)  for gradients,
0.0001 Angstrom      for optimized bond lengths,
0.001  deg           for optimized bond angles,
0.001  kcal/mol      for zero-point vibrational energies.
Normally such differences should be at least an order of
magnitude smaller, for the test jobs and reference outputs
provided. In the *.grep files, the gradients are numerically
the most sensitive data.

3.4.  Standard test jobs.

There are 50 input files for test jobs which are designed to
cover most of the major options in the program. These jobs are
grouped as follows.

job1*: Single-point SCF energy calculations for different methods.
job2*: Single-point SCF energy and gradient calculations.
job3*: SCF geometry optimizations and transition state searches.
job4*: Force constant analysis (combined with optimizations).
job5*: Reaction paths and grids.
job6*: Calculations with correlated wave functions.
job7*: Property evaluations.
job8*: Special features.

Characterization of the individual test jobs.

job1a: MNDO, ethylene
job1b: AM1 , ethylene
job1c: PM3 , ethylene
job1d: OM1 , ethylene
job1e: OM2 , ethylene
job1f: MNDO, ethylene cation, UHF
job1g: CNDO/2, ethylene cation, half-electron
job1h: ODM2, ethylene
job1i: ODM3, ethylene

job2a: MNDO, tetracene,  30 atoms,  84 AOs
job2b: MNDO, C60      ,  60 atoms, 240 AOs
job2c: MNDO, C50H100  , 150 atoms, 300 AOs

job3a: MNDO, ethylene, minimum, BFGS
job3b: MNDO, tetracene, minimum, BFGS
job3c: MNDO, oxygen triplet (UHF), minimum, BFGS
job3d: MNDO, H2CO->HCOH, TS, gradient norm minimization, internal  coords
job3e: MNDO, H2CO->HCOH, TS, gradient norm minimization, Cartesian coords
job3f: MNDO, H2CO->HCOH, TS, eigenvector following (EF), internal  coords
job3g: MNDO, H2CO->HCOH, TS, eigenvector following (EF), Cartesian coords
job3h: MNDO, ethylene, minimum, EF algorithm, pure Newton-Raphson
job3i: MNDO, ethylene, minimum, EF algorithm, Newton-Raphson + BFGS
job3j: MNDO/d, Cl2/ClF3/CHCl3, minima, BFGS
job3k: MNDO/d, Na - Hg compounds, minima, BFGS, parameter check
job3l: MNDO/d, Ti(CH3)4/CuCl/ZrF4/HPdOH, minima, BFGS, parameter check

job4a: MNDO, hydrogen
job4b: MNDO, water, C1
job4c: MNDO, water, Cs
job4d: MNDO, formaldehyde, C2v
job4e: MNDO, ethylene, optimization + force constants, D2h
job4f: MNDO, hydrogen peroxide, TS search + force constants, C2h
job4g: MNDO/d, CCl4, optimization + force constants
job4h: ODM2, ethylene, optimization + force constants, D2h
job4i: ODM3, ethylene, optimization + force constants, D2h

job5a: MNDO, methanol, path, internal rotation
job5b: MNDO, methanol, grid, explicit input
job5c: MNDO, methanol, grid, input of step size

job6a: MNDOC, ethylene, second-order perturbation theory (BWEN)
job6b: MNDOC, vinyl cation, BWEN, geometry optimization
job6c: MNDOC, vinyl cation, single-point BWEN after SCF optimization
job6d: MNDOC, methylene, BWEN1, geometry optimization
job6e: MNDO , tetracene, BWEN for pi-system only
job6f: MINDO/3, ethylene, minimal 3*3 CI

job7a: MNDO, ethylene, hyperpolarizability
job7b: AM1 , ethylene, single-point COSMO solvation energy
job7c: AM1 , glycine zwitterion, COSMO geometry optimization
job7d: MNDO, ethylene, NMR, single-point MNDO-B at input geometry
job7e: MNDO, ethylene, NMR, single-point MNDO-B after AM1 optimization

job8a: MNDO/d, phosphorus compds, evaluation with reference data
job8b: MNDO/H, water dimers, opt+force, evaluation with MP4 data
job8c: AM1, dimethylether, QM/MM, electrostatic potential and field
job8d: AM1, dimethylether, QM/MM, SCF with external points charges
job8e: MNDO, ethylene with special link atom for QM/MM, optimization
job8f: MNDO, water, keyword input, NMR and COSMO/NMR, MNDO-A
job8g: MNDO, ethylene, keyword input, DIIS in SCF

Comparison with previous program versions: For MNDO94 there have been
29 standard test jobs which are included in the current test suite
(even though in a different order). The MNDO99 results are consistent
with the MNDO94 results. Closer inspection shows that there are some
very minor numerical differences. These deviations are due to the
fact that MNDO94 employs numerical finite-difference derivatives
whereas MNDO99 makes use of analytic derivatives (whenever suitable).
The more accurate MNDO99 results agree with the MNDO94 results within
the numerical accuracy of the latter.

3.5.  MOPAC test jobs.

There are 8 input files which are taken from the standard test
input files for MOPAC(6.0) as provided in the QCPE version [26].
The following tables characterize these tests in more detail.

Name of input file   Calculations   Comments
MOPAC(6.0)  MNDO99   Total MNDO99

1scf       mopac61     16    13     Check electronic options
elements   mopac62     73    73     Check all elements
force      mopac63      6     6     Force constants
geometry   mopac64     16    11     Geometry optimizations
keys       mopac65      5     0     Special keywords
mnrsd1     mopac66      1     1     Standard test case
oldgeo     mopac67     15    15     Use of old geometries (a,b)
testdata   mopac68     11     9     Various options

(a) Keywords iscf=8 iplscf=8 have been added in run 13.
(b) Keyword RESTART has been removed in run 14.

The two columns under *Calculations* list the total number of
MOPAC test runs in a given input file and the corresponding number
of successful MNDO99 runs. Overall, 128 out of 143 test runs are
completed successfully when using program MNDO99. In the remaining
15 cases, the program stops after reading the keywords, with a
message identifying the unavailable keywords (e.g. HYPERFINE, ESR,
OPEN(4,3), MICROS, SADDLE, SIGMA, IRC, DRC).

The programs MNDO99 and MOPAC(6.0) always yield practically
identical heats of formations for a given fixed input geometry,
with typical deviations of the order of 0.00001 kcal/mol.
Similar deviations are encountered after geometry optimizations
with tight convergence criteria, e.g. GNORM=0.01, whereas
differences up to 0.001 kcal/mol may occur after optimizations
with the default convergence criteria. Optimized geometries
normally agree to better than 0.0001 angstrom and 0.01 degree
in the former case, and to 0.001 angstrom and 0.1 degree in the
latter case. With the default convergence criteria, MNDO99
often leads to slightly lower final heats of formation.
Vibrational frequencies usually agree to within 1 wavenumber,
and other quantities derived from the force field are also in
reasonable agreement (e.g. entropies and heat capacities).

3.6.  Possible modifications.

When parameters for additional elements become available (see
section 2.1), they may be included in the corresponding routines
which define the parameter values (e.g. blockdata and subroutines
PARAM, PARAMD, MPARAM, CPARAM).

The user may desire to define new symmetry conditions, on top
of those in subroutine SYMTRY (see section 5.3). This is done
easily by extending the code in subroutine SYMTRY.

There are some default options in the program code which may
be adapted to a given target machine. Choices are included in
the source code on comment lines with the string 'CSET'.
- DSTORE in subroutine INPANA: Number of external storage units
needed to double precision word on a direct-access file.
Default: DSTORE=8.0D0, i.e. use bytes as units.
This conforms with IBM-AIX and also works on SGI-IRIX when
using the f77 compiler option -bytereclen.
DSTORE is only needed in the analytic derivative section
for defining the record length of file iurhs (PSDRV, PSNMR).
- IDIAGV in subroutine INPUT: Default choice of diagonalization
routine in subroutine ITER, currently set to IDIAGV=0.
Note that this default may be overwritten by explicit input
for option idiag. Other possible values for idiag are 1-9
which may also be chosen as default for IDIAGV if this is
advantageous on a given machine (for more details, see input
description for idiag in file mndo99.txt).
- LM6VEC in subroutine DYNSCF: LM6VEC defines the vector length
above which it is faster to use subroutine FOCK instead of
FOCKX on a vector machine. LM6VEC=100 has been found suitable
for Cray vector machines. The current default LM6VEC=0 implies
a call to subroutine FOCKX which is appropriate for scalar
machines and will work correctly on any machine.
- IROTV in subroutine ROTD: Choice of method for rotating the
two-center two-electron spd integrals (see ROTD for details).
The current default IROTV=1 uses unrolled scalar code and is
best on scalar machines. IROTV=3 selects straight matrix
multiplications with many zero values and may be competitive
for vector machines.

The timing routine (CPUSEC) is machine-specific. The standard
version in the program refers to the library function ETIME
which is usually available on UNIX machines (e.g. SGI).
Alternative calls are included in CPUSEC as comments (for IBM,
Cray, NEC, Fujitsu, SNI, Convex) and may be activated as needed.

Finally the user may want to increase the buffers in program
MNDO99 in order to treat larger molecules than in the standard
version. All the information needed for such modifications is
given in section 4 and appendix B.

3.7.  Special information for Cray.

THIS SECTION IS TAKEN FROM THE MNDO94 DOCUMENTATION.
IT NEEDS TO BE UPDATED TO MNDO99 AFTER A CRAY INSTALLATION.

The executable file install contains the following commands.
fsplit mndo9941.ftn
cf77 -Zv -Wf"-dp" -c *.f
cc -c -V memx.c
segldr *.o -o mndo -V - <<'EOF'
dynamic=//
heap=400000+0
map=stat
EOF
cp mndo $HOME/bin/mndo
rm *.f

Comments.
- The use of the cf77 option -Zp (instead of -Zv) generates a
parallel version of the program (autotasking and microtasking).
- The source file mndo9941.ftn may also be compiled using the
option -a static (no difference in performance). Note, however,
that the default option -a stack is required for multitasking.
Option -dp is used for convenience.
- The dynamic memory management of blank common is handled by
Cray-specific C routines provided in file memx.c. If any
problems should arise, one may use a fixed size of blank common
by defining the variable len in the main program appropriately
(see parameter statements and comments) and by deleting the
calls to subroutine defmem from subroutine start.
- In the segldr directives, the heap has been fixed to 400000
words. This limit is large enough to handle the parallel
version of the program for 8 cpus. It may be decreased for
a single-processor version.

The procedure mndogo which is provided as a separate file may
be useful for running the program on a Cray Y-MP under Unicos.
It is intended to be self-explanatory. It should facilitate
file handling and restarts.

3.8.  Special information on files.

During execution the program needs an input file and an output
file (logical units 5 and 6, respectively). Depending on the
options chosen and on the available buffer (see section 4)
the program may need a number of additional sequential files
which are described in sections H-I of the input description
(see file mndo99.txt). These files are not opened in the Fortran
program so that the operating system will assign these files by
default unless the user assigns them by appropriate job control
commands.



## 4. Program size and memory allocation.

4.1.  General comments.

There are a number of parameters which determine the size of the
arrays in MNDO99 and, therefore, the size of the molecules that
can be studied (see appendix B for a complete list). The two most
important parameters are:
LM1       Maximum number of atoms.
LEN       Length of blank common used as general buffer.

Reasonable choices for these parameters are, for example:
(A)        (B)        (C)
LM1           150        300        600
LEN       1000000    3000000   10000000

The standard version of MNDO99 employs choice (C) where the buffer
needs up to 80 MB of memory (and the whole program up to 100 MB).
Note that floating point numbers are always represented as 64-bit
words (8 bytes).

If the user wants to change the standard dimensions, the statement
PARAMETER (LM1=600)
must be redefined throughout the whole program. The statement
PARAMETER (LEN=1000000)
appears only in the main program and should be modified to remain
consistent with the selected LM1 value.

On machines which allow for dynamic memory management, the blank
common area can be allocated dynamically (e.g. under Cray-UNICOS,
see subroutine DEFMEM for a previous implementation). The maximum
size of blank common will then depend on the maximum memory limit
for a given job and is determined by appropriate system calls.
On other machines, the length of blank common is defined in the
main program, through a PARAMETER statement for LEN (see above).
The following remarks refer to both cases since the maximum size
of blank common is always defined.

For a given molecule the program will automatically allocate the
buffer in blank common as efficiently as possible. If the blank
common area is too small for the most efficient in-core treatment
the program will use auxiliary files (involving disk input/output)
and may even employ slower algorithms requiring less memory. This
will be indicated by appropriate warnings in the output. If the
blank common area is still too small after these measures the
program will stop with an appropriate message.

It is strongly recommended to provide a buffer in blank common
which is large enough to carry out all operations in memory and
to avoid an internal switching to less efficient procedures.
This is accomplished by choosing a suitable length of the blank
common area (see above). To assist in this choice for larger
molecules a brief outline of the memory allocation is given in
the following sections. For more detail, the code in subroutines
DYNFOR, DYNSCF, DYNPT, DYNSCR, and DYNCSM should be consulted.

The actual memory allocation for a given calculation will be
printed on request (input option jprint>1).

4.2.  Use of blank common: Geometry optimization and SCF treatment.

The following discussion refers only to the most common case
(standard closed-shell SCF and gradient calculations without
analytic derivatives or other special features). Additional
remarks for other applications are given in sections 4.3-4.4.

Variables used for memory allocation in blank common.
NH                               number of hydrogen atoms
NX                               number of atoms with an sp basis
ND                               number of atoms with an spd basis
NUMAT  = NH+NX+ND                number of atoms
NVAR                             number of geometrical variables
LM2    = NH+4*NX+9*ND            number of basis functions
LFA                              buffer for optimization etc
LSA                              buffer for SCF treatment
LM9                              buffer for two-electron integrals
LM5    = LFA+LSA+LM9             buffer length (total)

LFA is usually much smaller than LSA and LM9.
LFA    = NVAR*(NVAR+1)/2         optimization for minimum
LFA    = 2*NVAR*NVAR+NVAR        optimization for transition state
LFA    = 9*NUMAT*(NUMAT+1)       force constant calculation
LFA    = 0                       otherwise

LSA depends on the type of SCF calculation. For even LM2 we have
LSA    = 4*LM2*LM2 + 5*LM2/2     for RHF calculations
LSA    = 7*LM2*LM2 + 9*LM2/2     for UHF calculations

LM9 depends on the semiempirical method used.
LM9    = NUMAT*(NUMAT+1)/2       for MINDO and CNDO
LM9    = (45*ND+10*NX+NH)**2     for MNDO and related methods
LM9 can be defined via input in the case of MNDO-type methods
(see input variable imode) which enforces disk input/output of
the two-electron integrals using a buffer of length
LM9    = IMODE*512

For easy reference the following table lists the buffer lengths
for molecules of different size. The information in this table
should be useful for defining suitable values of LEN (see above)
by requiring LEN>LM5, LM5=LFA+LSA+LM9. ND=0 is assumed.

NH   NX   LM2   LSA(RHF)  LSA(UHF)  LM9(MNDO)
10   10    50     10125     17725     12100
20   20   100     40250     70450     48400
30   30   150     90375    158175    108900
40   40   200    160500    280900    193600
50   50   250    250625    438625    302500
60   60   300    360750    631350    435600
80   80   400    641000   1121800    774400
100  100   500   1001250   1752250   1210000
150  150   750   2251875   3940875   2722500
200  200  1000   4002500   7004500   4840000
300  300  1500   9003750  15756750  10890000
400  400  2000  16005000  28009000  19360000
500  500  2500  25006250  43761250  30250000

If the available buffer in the blank common area is smaller
than required for an in-core treatment (i.e. LEN < LM5)
the program will first reduce the buffer for the two-electron
integrals using LM9=5120 and disk input/output. In the case
of RHF calculations, this reduces the required memory by about
a factor of 2 (see above) and leads only to a moderate increase
of computation times. If the available buffer is then still too
small the program will decrease LFA and/or LSA. This yields
only a comparatively small reduction of the required memory
and a relatively large increase of computation times so that
this situation should be avoided, if possible, by a suitable
choice of LEN.

4.3.  Use of blank common: Second-order perturbation theory.

In the MNDOC method, electron correlation is treated explicitly
by second-order perturbation theory (e.g. BWEN, option kci).
In the chosen implementation, this requires a transformation of
the two-electron integrals from the AO basis to the MO basis.
Subroutine DYNPT allocates the blank common area accordingly.
The buffer starts at the same address as the SCF buffer and
leaves the first two RHF arrays (eigenvectors and eigenvalues)
unchanged (since these are also needed in the transformation
and the perturbational calculation). The other RHF-SCF arrays
will be overwritten, in general. The density matrix is normally
needed again in later calculations and is therefore saved on
disk, if necessary.

The memory allocation scheme in subroutine DYNPT first attempts
an in-core treatment. If there is not enough memory available,
disk I/O is employed for the intermediate arrays to reduce the
memory requirements. If this does not help, the calculation is
aborted. The memory allocation in subroutine DYNPT is automatic
and proceeds without user intervention.

4.4.  Use of blank common: Other tasks.

After assigning the buffer for the geometry optimization and
the SCF treatment (see section 4.2), the blank common area is
allocated up to address LM5. Buffer space beyond address LM5
may be used in the perturbation treatment (see section 4.3)
which, however, is local to subroutine PERT (called from SCFCAL)
and therefore does not interfere with other tasks.

The buffer space beyond address LM5 is thus available for use
in other parts of the program, in particular:
(a) Scratch arrays in the analytic derivative section.
(b) Additional SCF arrays in OM1 and OM2.
(c) Scratch arrays for the COSMO solvation treatment.
(d) Scratch arrays for the DIIS SCF converger.

The analytic derivative code (a) has its own internal memory
allocation which is quite intricate and flexible. It employs
the blank common area between addresses LM5+1 and LEN, and it
is strictly local in the sense that the arrays (a) "live" only
when the analytic derivative routines are being executed (i.e.
during the calls to PSDRV from SCF or FMTRXA and the call to
PSNMR from MNDO99). No buffer space is needed for the analytic
gradient of variational wavefunctions, whereas approximately
20*LM2**2 and 30*LM2**2 words are required for the efficient
analytic computation of nonvariational gradients and second
derivatives, respectively.

The OM1 and OM2 methods (b) employ four extra arrays during
integral evaluation (subroutine HCORE called from SCFCAL).
Three of these arrays hold LM4=LM2*(LM2+1)/2 words, and the
fourth one LM2*NUMAT words. They start at address LM5+1.
The gradient calculation in OM1 and OM2 needs five additional
arrays of similar size which are appended after the first four
arrays (subroutine DCART2 called from SCF). Subroutine DYNSCR
checks whether the available memory is sufficient, and then
assigns all addresses. In both stages (HCORE, DCART2) the
extra arrays are local. However, between these two stages, the
buffer space beyond LM5 may also be accessed by other tasks
such as (c) and (d). In the case of memory contention, the
first four extra arrays are either saved on disk or recomputed
when needed (for details, see code).

The COSMO solvation treatment (c) uses buffer space beyond LM5
on several occasions: Before integral evaluation (subroutines
CONSTS and DMAT called from SCFCAL), during integral evaluation
(subroutines ADDHCR and ADDNUC called from SCFCAL), during the
SCF iterations (subroutine ADDFCK called from ITER), and in the
gradient calculation (subroutine DGRAD called from SCF). While
the first and last stage employ local arrays, the second and
third one may coexist with other tasks such as (b) or (d). In
such cases, COSMO data will automatically be stored on disk
(if necessary). Minimum memory consumption by COSMO can also
be enforced via input (option modcsm=2). For more information,
see subroutine DYNCSM.

The DIIS convergence acceleration (d) again employs the buffer
space beyond LM5, for holding previous Fock and error matrices
which are needed in the DIIS extrapolation procedure. The
DIIS section attempts to reserve as much memory as possible
between addresses LM5+1 and LEN (for improved extrapolations
and efficiency). The DIIS arrays (d) must "live" through the
SCF iterations and may thus coexist with arrays (b) and (c).

Generally speaking, the assignment of the scratch space beyond
LM5 is rather straightforward if there is only a single active
task. Difficulties may arise when more than one tasks tries
to access the scratch space. It is believed that the MNDO99
code resolves any possible memory contention between (a)-(d).
For more information, the reader should consult the source code,
in particular subroutine DYNSCR. As mentioned before, the actual
memory allocation will be printed for option jprint>1.



## 5. Comments on input options.

The input to program MNDO99 is described in file mndo99.txt.
This section of the documentation reviews the available modes
of input and attempts to give background information on certain
input options. It is quite incomplete, but it is hoped that the
user may benefit from some remarks addressing points which might
remain unclear otherwise.

Generally speaking it is recommended to use the default values
of the options in the program as much as possible. The input
for the test jobs (see input files) provides examples on what
is considered to be reasonable input.

5.1.  Available modes of input.

There are three modes of input for this program.

- Standard input based on standard MNDO-style numerical data.
- Keyword  input based on keywords and MNDO-style numerical data.
- MOPAC    input based on keywords and MOPAC-style numerical data.

The standard input allows the user to access all options of the
program. It is fully specified in sections C-D of the input
description (see file mndo99.txt).

The keyword input is equivalent to the standard input. It consists
of a keyword section (up to ten lines of MNDO99 keywords and two
lines of text) and standard MNDO-style numerical data for the
remainder. MNDO99 keywords have the format <keyword>=<value>
where <keyword> denotes the name of any input variable in the
standard input, and <value> is the actual input value.

The MOPAC input is provided to allow the use of MOPAC input files.
It consists of a keyword section (up to three lines of keywords
and two lines of text) and MOPAC-style data for the remainder.
The input routines are adapted from program MOPAC(6.0) written by
J.J.P.Stewart. Most common keywords are recognized by this program
and converted to options of the standard input. Some keywords are
not available. In this case the program will print an appropriate
message and then either stop or ignore the keyword. The treatment
of all MOPAC(6.0) keywords is fully specified in section G of the
input description. The MOPAC input for geometry and symmetry (etc)
is the same as in MOPAC(6.0), see MOPAC manual [26].

A number of options in the program are not accessible when using
only the genuine MOPAC keywords. To overcome this limitation,
MNDO99 keywords can be combined with genuine MOPAC keywords to
ensure that all options of the program can be accessed through
MOPAC-style input.

The program automatically determines the mode of input from the
contents of the input file. It checks the first three lines for
characters A-Z or a-z (columns 1-80 of lines 1-2 and columns 1-30
of line 3). If such characters are found, the program attempts to
recognize MNDO99 and MOPAC keywords. The mode of input is then
assigned as follows.
- Standard input: No characters A-Z or a-z are found.
- Keyword  input: Characters A-Z or a-z appear, and there are
only MNDO99 keywords.
- MOPAC    input: Characters A-Z or a-z appear, and there is
at least one genuine MOPAC keyword.

By default, the standard input is formatted. For the sake of
convenience, however, there is an option to employ input in
free format for the geometry, symmetry, and other molecular data
(see option iform).

5.2.  Cartesian vs. internal coordinates.

The program allows to define geometries in terms of cartesian
or internal coordinates (see variable igeom), the latter
being default. In both cases it is possible to impose symmetry
relations between variables (see section 5.3) and to specify
certain variables to be fixed in geometry optimizations. Both
types of coordinates are therefore treated equivalently in the
program.

In calculations at fixed input geometries, it is a matter of
convenience to choose between cartesian and internal coordinate
input. In geometry optimizations, however, cartesian coordinates
tend to be coupled more strongly than well-defined internal
coordinates so that the latter ones are preferred in this regard.
When using cartesian coordinates in geometry optimizations, one
should take care that only 3n-6 coordinates are varied in the
optimization.

When defining the geometry in terms of internal coordinates, the
first atom is automatically put into the origin, the second atom
on the positive x-axis, and the third atom into the xy-plane.
Starting with the fourth atom, three reference atoms must be
given for defining a new atom, and the proper choice of these
reference atoms is very important for reasonable definitions.
Three other points should be mentioned.
- For bond angles other than 0 or 180 degrees, the reference
atoms must not lie on a line because then the dihedral angle
cannot be calculated, and the program will terminate with an
error.
- The use of dummy atoms is highly encouraged for defining
geometries in terms of internal coordinates.
- For complicated cases it is recommended to check the input
geometries using option kgeom=-1 before starting a costly
calculation.

5.3.  Symmetry conditions.

The program allows to specify symmetry relations between a
reference atom (L1) and dependent atoms (L3), both in internal
and cartesian coordinates, the type of relation being defined
by the symmetry relation number (L2).

For example, the bond length for atom L3 can be set equal to
the bond length for atom L1 (case L2=1), or the same can be
done for the bond angle (L2=2) or the dihedral angle (L2=3).
Analogously, for cartesian coordinates, L2=1 (2,3) implies
equality of the corresponding x (y,z) coordinates. There are
33 predefined symmetry relations in subroutine SYMTRY which
are specified in the input description (see file mndo99.txt).
The most useful symmetry relations are those for L2=1,2,3,14.

5.4.  Automatic detection of symmetry.

The program checks the symmetry of the molecule on several
occasions in order to exploit symmetry for a reduction of the
computational costs. This is done
- in the numerical calculation of cartesian gradients,
- in the numerical calculation of cartesian force constants,
- in the second-order perturbation treatment of correlation.

In all these cases the molecule is translated such that the
center of gravity lies in the origin, but no rotations are
carried out. The program then checks whether the cartesian
axes are C2 axes and whether the cartesian planes are planes
of symmetry, the criterion being an agreement between the
corresponding cartesian coordinates of at least 0.0000001
angstrom. Based on this information the program assigns the
molecule to an abelian point group (C1,Cs,C2,C2v,D2h,C2h,
D2,Ci) and uses this information for simplifying the
calculation.

This procedure has been described to make two points.
- By defining the molecule in a suitable orientation (possibly
via dummy atoms), the user can influence the computation
times for symmetric molecules, especially in force constant
calculations and in MNDOC BWEN studies.
- In the case of degenerate point groups, the user should not
worry about output indicating that the program has detected
only an abelian subgroup (see above). The calculation will
be correct, but will exploit only part of the molecular
symmetry in the calculation.

There is one subroutine (SYMNUM) in the program where the
symmetry assignments are done in principal-axes coordinates
with additional information from the principal moments. In
this subroutine the correct point group of the molecule must
be found to define the symmetry number for the rotational
partition function in the calculation of thermodynamic
properties. The code in subroutine symnum has been found to
work for most point groups, but fails in certain complicated
cases (e.g. point groups Dn and Dnd with even n). For these
cases explicit input of the symmetry number is required (see
input option numsym).

Symmetry may also be exploited in SCF calculations by specifying
orbital occupation numbers for each irreducible representation
(see input option abs(iuhf)=3). It is thus possible to converge
the SCF solution for the lowest state of a given symmetry (only
Abelian groups or subgroups). This option should be used with
caution since it has been tested only for a limited number of
cases. In particular, problems with SCF convergence occur when
unreasonable occupations are defined (corresponding to highly
excited states). The implementation of this option does NOT
employ symmetry-adapted basis functions, but simply assigns
the symmetry of all orbitals in each SCF iteration and forces
the orbitals to be occupied as specified via input. If this is
not possible for any reason, the program stops.

5.5.  Geometry optimizations.

There are several options to carry out geometry optimizations for
energy minima. Quasi-Newton optimization techniques are used by
default. Systematic studies have shown [27] that the BFGS update
with a fairly inaccurate line search is superior to the original
DFP update with a fairly accurate line search, the computational
savings being around a factor of 2. Hence, BFGS is chosen by
default, but DFP is still available via input (option idfp).

While the algorithm for finding energy minima is quite robust
a successful search for transition states still requires a 
good starting geometry. Gradient norm minimization (default)
and eigenvector following (option ief) are available for the
location of transition states. If both techniques fail to find
a transition state, the optimization should be attempted again
with a refined initial geometry.

It is often useful to carry out a geometry optimization at
the SCF level followed by a single-point calculation at the
correlated level using the optimized SCF geometry. This can
be done by choosing a negative input value for option kci.

5.6.  Restarts.

Geometry optimizations and force constant calculations can
be restarted (see option middle) provided that the results
from the previous run have been saved on a permanent file
(logical unit 4). The program automatically saves restart
data on this file, but the restart is only possible, of
course, if this file has been made permanent by the user.
This is recommended for large calculations.

5.7.  Diagonalization routines.

In general, diagonalizations use standard library routines. Since
diagonalizations are usually the time-determining step in standard
semiempirical SCF calculations, special efforts have been made to
speed up this step.

As far as possible we use the pseudodiagonalization scheme [28]
in subroutine DIAG. The input option ifast=2 may be chosen to
avoid using subroutine DIAG (e.g. for checking any errors) which,
however, increases the computation times significantly. The input
option ifast=1 ensures that normal diagonalizations are carried
out at the beginning and at the end of each SCF calculation. The
default option ifast=0 avoids these normal diagonalizations during
intermediate SCF calculations in geometry optimizations and force
constant calculations by using the eigenvectors of the previous
SCF calculation in subroutine DIAG (provided that there is enough
memory). This default procedure may occasionally lead to an error
in subroutine DIAG (negative argument of sqrt), especially if the
new geometry differs strongly from the previous one. This error
with ifast=0 can be avoided using ifast=1. It occurs so rarely,
however, that the default option ifast=0 is recommended for the
sake of efficiency.

Normal diagonalizations in subroutine iter may be carried out
by one of nine methods according to the input option idiag.
- idiag=0   treated as idiag=9 in most program versions,
except when optimized library routines provide
superior performance for other values of idiag.
- idiag=1   eispack routines (TRED3,TQL2,TRBAK3).
- idiag=2   eispack routines (TRED2,TQL2).
- idiag=3   lapack routines (driver DSPEV).
- idiag=4   lapack routines (driver DSPEVX).
- idiag=5   lapack routines (driver DSYEV).
- idiag=6   lapack routines (driver DSYEVX).
- idiag=7   lapack routines (driver DSPEVD), divide-and-conquer.
- idiag=8   lapack routines (driver DSYEVD), divide-and-conquer.
- idiag=9   eispack-based routines (TRED1,EQLRAT,EINVIT,TRBAK1)
from S.T.Elbert [29].

Options idiag=2,5,6,8,9 work with a square matrix that needs to
be diagonalized, whereas options idiag=1,3,4,7 employ a linearly
packed matrix.
Option idiag=1 (involving eispack routines TRED3, TQL2, TRBAK3)
is analogous to option idiag=2, but works with a linearly packed
array rather than a square matrix. It is slower than option
idiag=2 and should be used in the SCF part only if memory is
limited.
Option idiag=2 (involving eispack routines TRED2 and TQL2) is
a very robust diagonalization procedure and should be used
if numerical problems occur.
Options idiag=4,6,9 involve inverse iteration and should thus
be somewhat faster than options idiag=1,2,3,5 - particularly
when not all of the eigenvectors are needed. Measurements show
that idiag=9 is usually fastest for smaller matrices (up to the
order of n=500) while idiag=6 is normally fastest for larger
cases (above n=500), among the methods that employ inverse
iteration.
Options idiag=7,8 involve a divide-and-conquer approach. They
may become faster than other approaches for large matrices, but
they require much more scratch space (i.e., more than 2*n*n for 
idiag=7 and more than 3*n*n for idiag=8), and they occasionally
fail to converge. idiag=8 is generally faster than idiag=7, at
the expense of using more memory.
Recommendation: Use idiag=9 up to n=500 and idiag=6 above n=500.
The findings reported are based on standard Fortran versions of
the diagonalization routines. Preferences may change if there
are optimized versions available (e.g., for lapack routines).

5.8.  SCF convergence criteria.

The program considers the SCF procedure to be converged if
for two consecutive SCF cycles
- the change in the energy is below 10**(-iscf) ev, and
- the change in all diagonal elements of the density matrix
is below 10**(-iplscf).
The default values for these criteria are iscf=6 and iplscf=6
which is normally sufficient for all standard applications.
These values may be redefined via input (options iscf, iplscf).

In geometry optimizations at the SCF level with low precision
(iprec=1), iscf=5 and iplscf=3 are often adequate which leads to
less SCF iterations and thus to lower computational costs. The
program uses these default values in such geometry optimizations.
More stringent SCF convergence criteria can be imposed via input
(options iscf, iplscf). An alternative reasonable choice for
such optimizations is iscf=6 and ipl=4 [26].



## 6. References.

1  W. Thiel, Adv.Chem.Phys. 93, 703 (1996).
2  J.J.P. Stewart, J.Comput.Aided Mol.Design 4, 1 (1990).
3  M.J.S.Dewar, J.Phys.Chem. 89, 2145 (1985).
4  M.J.S.Dewar and W.Thiel, J.Am.Chem.Soc. 99, 4899 (1977).
5  W.Thiel, J.Am.Chem.Soc. 103 (1981) 1413.
6  W.Thiel and A.A.Voityuk, Theoret.Chim.Acta 81 (1992) 391.
7  W. Thiel and A.A. Voityuk, J.Phys.Chem. 100, 616 (1996).
8  M.J.S.Dewar, E.G.Zoebisch, E.F.Healy, and J.J.P.Stewart,
J.Am.Chem.Soc. 107, 3902 (1985).
9  J.J.P.Stewart, J.Comput.Chem. 10, 209 (1989).
10  M.Kolb and W.Thiel, J.Comput.Chem. 14, 775 (1993).
11  W. Weber, Ph.D. Thesis, University of Zurich, 1996.
12  R.C.Bingham, M.J.S.Dewar, and D.H.Lo, J.Am.Chem.Soc. 97
1285 (1975).
13  J.A.Pople and G.A.Segal, J.Chem.Phys. 44, 3289 (1966).
14  K.Y.Burstein and A.N.Isaev, Theoret.Chim.Acta 64, 397 (1984).
A.Goldblum, J.Comp.Chem. 8, 835 (1987).
15  C.C.J.Roothaan, Rev.Mod.Phys. 23, 69 (1951).
16  J.A.Pople and R.K.Nesbet, J.Chem.Phys. 22, 571 (1954).
17  M.J.S.Dewar, J.A.Hashmall, and C.G.Venier, J.Am.Chem.Soc.
90, 1953 (1968).
18  S.Schroeder and W.Thiel, J.Am.Chem.Soc. 108 (1986) 7985.
19  S.Patchkovskii and W.Thiel, Theor.Chim.Acta 93, 87 (1996).
20  S.Patchkovskii and W.Thiel, Theor.Chem.Acc. 98, 1 (1997).
21  S.Patchkovskii and W.Thiel, J.Comp.Chem. 11, 1318 (1996).
22  G.P.Ford and B.Wang, J.Comp.Chem. 14, 1101 (1993).
23  D.Bakowies and W.Thiel, J.Comp.Chem. 17, 87 (1996).
24  S.Patchkovskii, Ph.D. Thesis, University of Zurich, 1997.
25  A.Gelessus, Ph.D. Thesis, University of Zurich, 1997.
26  J.J.P.Stewart, Program MOPAC, Version 6.0, 1990.
27  W.Thiel, J.Mol.Struct. 163, 415 (1988).
28  J.J.P.Stewart, P.Csaszar, and P.Pulay, J.Comput.Chem.
3, 227 (1982).
29  S.T.Elbert, Theoret.Chim.Acta 71, 169 (1987).


------------------------------------------------------------------------


Appendix.


A.    Parameters.

This section defines the source of the parameters used in MNDO99.

A.1.  MNDO (iop=0)

H : M.J.S.Dewar, W.Thiel, J.Am.Chem.Soc. 99, 4899 (1977).
He: M.Kolb, W.Thiel, J.Comp.Chem. 14, 37 (1993).
Li: W.Thiel, QCPE Program no. 438, QCPE Bull. 2, 63 (1982).
Be: M.J.S.Dewar, H.S.Rzepa, J.Am.Chem.Soc. 100, 777 (1978).
B : M.J.S.Dewar, M.L.McKee, J.Am.Chem.Soc. 99, 5231 (1977).
C : M.J.S.Dewar, W.Thiel, J.Am.Chem.Soc. 99, 4899 (1977).
N : M.J.S.Dewar, W.Thiel, J.Am.Chem.Soc. 99, 4899 (1977).
O : M.J.S.Dewar, W.Thiel, J.Am.Chem.Soc. 99, 4899 (1977).
F : M.J.S.Dewar, H.S.Rzepa, J.Am.Chem.Soc. 100, 777 (1978).
Mg: A.A.Voityuk, Zhurnal Strukturnoi Khimii 28, 128 (1987).
Al: L.P.Davis, R.M.Guidry, J.R.Williams, M.J.S. Dewar, H.S.Rzepa,
J.Comp.Chem. 2, 433 (1981).
Si: M.J.S.Dewar, J.Friedheim, G. Grady, E.F.Healy, J.J.P.Stewart,
Organometallics 5, 375 (1986).
P : M.J.S.Dewar, M.L.McKee, H.S.Rzepa, J.Am.Chem.Soc. 100, 3607 (1978).
S : M.J.S.Dewar, C.H.Reynolds, J.Comp.Chem. 7, 140 (1986).
Cl: M.J.S.Dewar, H.S.Rzepa, J.Comp.Chem. 4, 158 (1983).
Zn: M.J.S.Dewar, K.M.Merz, Organometallics 5, 1494 (1986).
Ge: M.J.S.Dewar, G.L.Grady, E.F.Healy, Organometallics 6, 186 (1986).
Br: M.J.S.Dewar, E.F.Healy, J.Comp.Chem. 4, 542 (1983).
Sn: M.J.S.Dewar, G.L.Grady, J.J.P.Stewart, J.Am.Chem.Soc. 106,
6771 (1984).
I : M.J.S.Dewar, E.F.Healy, J.J.P.Stewart, J.Comp.Chem. 5, 358 (1984).
Hg: M.J.S.Dewar, G.L.Grady, K.M.Merz, J.J.P.Stewart,
Organometallics 4, 1964 (1985).
Pb: M.J.S.Dewar, M.K.Holloway, G.L.Grady, J.J.P.Stewart,
Organometallics 4, 1973 (1985).

A.2.  AM1 (iop=-2)

H : M.J.S.Dewar, E.G.Zoebisch, E.Healy, J.J.P.Stewart,
J.Am.Chem.Soc. 107, 3902 (1985).
B : M.J.S.Dewar, C.Jie, E.G.Zoebisch, Organometallics 7, 513 (1988).
C : M.J.S.Dewar, E.G.Zoebisch, E.Healy, J.J.P.Stewart,
J.Am.Chem.Soc. 107, 3902 (1985).
N : M.J.S.Dewar, E.G.Zoebisch, E.Healy, J.J.P.Stewart,
J.Am.Chem.Soc. 107, 3902 (1985).
O : M.J.S.Dewar, E.G.Zoebisch, E.Healy, J.J.P.Stewart,
J.Am.Chem.Soc. 107, 3902 (1985).
F : M.J.S.Dewar, E.G.Zoebisch, J.Mol.Struct. 180, 1 (1988).
Na: E.N.Brothers, K.M.Merz, J.Phys.Chem. B 106, 2779 (2002).
Mg: M.C.Hutter, J.R.Reimers, N.S.Hush, J.Phys.Chem. B 102, 8080 (1998).
Al: M.J.S.Dewar, A.J.Holder, Organometallics 9, 508 (1990).
Si: M.J.S.Dewar, C.Jie, Organometallics 6, 1486 (1987).
P : M.J.S.Dewar, C.Jie, J.Mol.Struct. 187, 1 (1989).
S : M.J.S.Dewar, Y.-C.Yuan, Inorg.Chem. 29, 3881 (1990).
Cl: M.J.S.Dewar, E.G.Zoebisch, J.Mol.Struct. 180, 1 (1988).
Zn: M.J.S.Dewar, K.M.Merz, Organometallics 7, 522 (1988).
Ge: M.J.S.Dewar, C.Jie, Organometallics 8, 1544 (1987).
Br: M.J.S.Dewar, E.G.Zoebisch, J.Mol.Struct. 180, 1 (1988).
Sn: M.J.S.Dewar E.F.Healy, D.R.Kuhn, A.J.Holder,
Organometallics 10, 431 (1991).
I : M.J.S.Dewar, E.G.Zoebisch, J.Mol.Struct. 180, 1 (1988).
Hg: M.J.S.Dewar, C.Jie, Organometallics 8, 1547 (1989).

A.3.  PM3 (iop=-7)

H : J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
Li: E.Anders, R.Koch, P.Freunscht, J.Comp.Chem. 14, 1301 (1993).
Be: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
C : J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
N : J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
O : J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
F : J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
Na: E.N.Brothers, K.M.Merz, J.Phys.Chem. B 106, 2779 (2002).
Mg: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Al: J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
Si: J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
P : J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
S : J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
Cl: J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
Zn: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Ga: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Ge: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
As: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Se: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Br: J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
Cd: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
In: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Sn: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Sb: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Te: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
I : J.J.P.Stewart, J.Comp.Chem. 10, 209 (1989).
Hg: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Tl: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Pb: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).
Bi: J.J.P.Stewart, J.Comp.Chem. 12, 320 (1991).

A.4.  MNDOC (iop=-1)

Parameters for H,C,N,O,F are taken from:
W.Thiel, J.Am.Chem.Soc. 103, 1413 (1981).

A.5.  MNDO/d (iop=-10)

Na: W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
Mg: W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
Al: W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
Si: W.Thiel, A.A.Voityuk, J.Mol.Struct. 313, 141 (1994).
P : W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
S : W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
Cl: W.Thiel, A.A.Voityuk, Int.J.Quant.Chem. 44, 807 (1992).
Zn: W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
Br: W.Thiel, A.A.Voityuk, Int.J.Quant.Chem. 44, 807 (1992).
Cd: W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
I : W.Thiel, A.A.Voityuk, Int.J.Quant.Chem. 44, 807 (1992).
Hg: W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
Na: W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).
Na: W.Thiel, A.A.Voityuk, J.Phys.Chem. 100, 616 (1996).

A.6.  OM1 (iop=-5)

Parameters for H,C,N,O,F are taken from:
M.Kolb, W.Thiel, J.Comp.Chem. 14, 775 (1993).

A.7.  OM2 (iop=-6)

Parameters for H,C,N,O are taken from:
W.Weber, Ph.D. Thesis, University of Zurich, 1996.

A.8.  OM3 (iop=-8)

Parameters for H,C,N,O are taken from:
M.Scholten, Ph.D. Thesis, University of Dusseldorf, 2003.

Parameters for F are taken from:
R.Steiger, Ph.D. Thesis, University of Zurich, 2003.

A.9.  MINDO/3 (iop=1)

Parameters for H,B,C,N,O,F,Si,P,S,Cl are taken from:
R.C.Bingham, M.J.S.Dewar, D.H.Lo, J.Am.Chem.Soc. 97, 1285 (1975).

A.10  CNDO/2 (iop=2)

Parameters for H,Li,Be,B,C,N,O,F are taken from:
J.A.Pople, G.A.Segal, J.Chem.Phys. 44, 3289 (1966).

A.11  Special MNDO variants (iop=-4)

Original parameters for Si and S (iparok=4) from:
M.J.S.Dewar, M.L.McKee, H.S.Rzepa, J.Am.Chem.Soc. 100, 3607 (1978).
Superseded by later developments (references see section A.1).

Specific carbon parameters for fullerenes (iparok=6) from:
S.Tseng, M.Shen, C.Yu, Theor.Chim.Acta 92, 269 (1995).
Table I, set B.

MNDO/PDDG parameters for H, C, N and O (iparok=8) from:
M.P.Repasky, J.Chandrasekhar, W.L.Jorgensen,
J.Comp.Chem. 23, 1601 (2002).

MNDO/PDDG parameters for F, Cl, Br and I (iparok=8) from:
I.Tubert-Brohman, C.R.W.Guimares, M.P.Repasky, W.L.Jorgensen,
J.Comp.Chem., in press.

A.12  Special PM3 variants (iop=-7)

PM3/PDDG parameters for H, C, N and O (iparok=8) from:
M.P.Repasky, J.Chandrasekhar, W.L.Jorgensen,
J.Comp.Chem. 23, 1601 (2002).

PM3/PDDG parameters for F, Cl, Br and I (iparok=8) from:
I.Tubert-Brohman, C.R.W.Guimares, M.P.Repasky, W.L.Jorgensen,
J.Comp.Chem., in press.

A.13  Semiempirical electrostatic potentials (mmpot=4-6)

Parameters for H,C,N,O in MNDO and AM1 (unpublished: Li, MNDO).
mmpot=4: D.Bakowies, W.Thiel, J.Comp.Chem. 17, 87 (1996).
mmpot=5: D.Bakowies, W.Thiel, J.Comp.Chem. 17, 87 (1996).

Parameters for H,C,N,O,F,Cl in AM1:
mmpot=6: G.P.Ford, B.Wang, J.Comp.Chem. 14, 1101 (1993).

A.14  Cavitation and dispersion terms in COSMO (icosmo=2,4)

Parameters for H,C,N,O,F,P,S,Cl in AM1 (solvent water) from:
A.Gelessus, Ph.D. Thesis, University of Zurich, 1997.

A.15  GIAO-MNDO for NMR chemical shifts (nmr=1,2,11,12)

Parameters for H,C,N,O (methods A and B) from:
S.Patchkovskii, Ph.D. Thesis, University of Zurich, 1997.
S.Patchkovskii, W.Thiel, J.Comp.Chem. 20, 1220 (1999).



B.    Limitations of the program.

The maximum size of the arrays in MNDO99 is defined in
PARAMETER statements in the main program. These statements
are repeated throughout the code in subroutines (as needed).

B.1.  Predefined limits.

LEN      Length of blank common.
LM1      Maximum number of atoms.
LMR      Maximum number of points on reaction path (LMR).
LMG      Maximum number of points on reaction grid (LMG,LMG).
LMZ      Maximum atomic number.
LMK      Maximum number of ECP operators (OM1).
LML      Maximum number of ECP data sets (OM1).
LMF      Maximum number of reference data.
LMM      Maximum number of reference molecules.
LMPR     Maximum number of reference properties.
LMP      Maximum number of external input parameters.
LMNPS    Maximum number of segments on COSMO surface.
LM1M     Maximum number of external points.
MXNICS   Maximum number of NICS points for NMR.

The following values are used in MNDO99:
LEN    = 10000000
LM1    = 600
LMR    = 200            used with option kgeom=1
LMG    = 25             used with option kgeom=2
LMZ    = 86
LMK    = 200            used with option iop=-5
LML    = 100            used with option iop=-5
LMF    = 3000           used with option inrefd=1
LMM    = 400            used with option inrefd=1
LMPR   = 50             used with option inrefd=1
LMP    = 200            used with option iparok=1-3
LMNPS  = 1000           used with option icosmo.ne.0
LM1M   = 1000           used with option mminp=1,2
MXNICS = 500            used with option nmr.ne.0

The most important limits (LEN,LM1) have been described in
section 4 since they mainly determine the size of the molecules
that can be studied (as well as the memory requirements of the
program). Most of the other limits are associated with linear
arrays and can therefore be increased without increasing the
memory demands too much. LMNPS is used in two-dimensional COSMO
arrays and should therefore be increased only with care.

B.2.  Derived limits.

LMI      Maximum number of unique AO pairs in the molecule.
LME      Maximum number of exchange indices in the molecule.
LMX      Maximum number of basis orbitals for index array.
LMV      Maximum number of geometrical variables.
LMS      Maximum number of symmetry relations.
LMGP     Maximum number of Gaussian primitives (OM1/OM2).
LMGS     Maximum number of Gaussian shells (OM1/OM2).

Definitions:
LMI    = 45*LM1    appropriate for spd basis
LME    = 81*LM1    appropriate for spd basis
LMX    = 9*LM1     appropriate for spd basis
LMV    = 3*LM1     always appropriate
LMS    = 3*LM1     always appropriate
LMGP   = 6*LM1     appropriate up to STO-6G expansions
LMGS   = LM1       appropriate for minimal valence basis