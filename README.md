server.yaml
===========

To use this it will look for server.yaml in $ROS_HOME/buildfarm for credentials.  Put your Jenkins login in this file.

 * url: http://10.210.9.131:8080/jenkins
 * username: USERNAME
 * password: PASSWORD

Reconfiguring Jenkins
=====================

To reconfigure Jenkins run the create_release_jobs.py script.

If you do not specify a custom workspace the gbp repositories will be cached under /tmp/repo-workspace-ROSDISTRO, so that you only have to update not clone the whole repo every time.

    scripts/create_release_jobs.py groovy --commit

If a package has been renamed or removed use the --delete option to remove jobs other than the ones just configured.

Triggering new builds
=====================

Once you have made a new release into a gbp repo, and updated the version number in the rosdistro.yaml file.  Run trigger_missing.py

    scripts/trigger_missing.py --sourcedeb-only groovy --commit

To retrigger all job generating Debian packages where the package does not yet exist run:

    scripts/trigger_missing.py groovy --commit


Load Averages
=============

Three graphs 10sec, 3 min, 15 min rolling averages.

indigo_debbuild
---------------

![Indigo Load](http://lcas.lincoln.ac.uk/jenkins/label/indigo_debbuild/loadStatistics/graph?type=sec10&width=280&height=200 "indigo_debbuild") ![Indigo Load](http://lcas.lincoln.ac.uk/jenkins/label/indigo_debbuild/loadStatistics/graph?type=min&width=280&height=200 "indigo_debbuild") ![Indigo Load](http://lcas.lincoln.ac.uk/jenkins/label/indigo_debbuild/loadStatistics/graph?type=hour&width=280&height=200 "indigo_debbuild") 

hydro_debbuild
--------------

![Hydro Load](http://lcas.lincoln.ac.uk/jenkins/label/hydro_debbuild/loadStatistics/graph?type=sec10&width=280&height=200 "hydro_debbuild") ![Hydro Load](http://lcas.lincoln.ac.uk/jenkins/label/hydro_debbuild/loadStatistics/graph?type=min&width=280&height=200 "hydro_debbuild") ![Hydro Load](http://lcas.lincoln.ac.uk/jenkins/label/hydro_debbuild/loadStatistics/graph?type=hour&width=280&height=200 "hydro_debbuild") 

groovy_debbuild
---------------

![Groovy Load](http://lcas.lincoln.ac.uk/jenkins/label/groovy_debbuild/loadStatistics/graph?type=sec10&width=280&height=200 "groovy_debbuild") ![Groovy Load](http://lcas.lincoln.ac.uk/jenkins/label/groovy_debbuild/loadStatistics/graph?type=min&width=280&height=200 "groovy_debbuild") ![Groovy Load](http://lcas.lincoln.ac.uk/jenkins/label/groovy_debbuild/loadStatistics/graph?type=hour&width=280&height=200 "groovy_debbuild") 

debbuild
--------

Generic jobs and Groovy dry

![Debbuild Load](http://lcas.lincoln.ac.uk/jenkins/label/debbuild/loadStatistics/graph?type=sec10&width=280&height=200 "debbuild") ![Load](http://lcas.lincoln.ac.uk/jenkins/label/debbuild/loadStatistics/graph?type=min&width=280&height=200 "debbuild") ![Load](http://lcas.lincoln.ac.uk/jenkins/label/debbuild/loadStatistics/graph?type=hour&width=280&height=200 "debbuild") 


devel
--------

Generic jobs and Groovy dry

![Devel Load](http://lcas.lincoln.ac.uk/jenkins/label/devel/loadStatistics/graph?type=sec10&width=280&height=200 "devel") ![Load](http://lcas.lincoln.ac.uk/jenkins/label/devel/loadStatistics/graph?type=min&width=280&height=200 "devel") ![Load](http://lcas.lincoln.ac.uk/jenkins/label/devel/loadStatistics/graph?type=hour&width=280&height=200 "devel") 

doc
--------

Generic jobs and Groovy dry

![Doc Load](http://lcas.lincoln.ac.uk/jenkins/label/doc/loadStatistics/graph?type=sec10&width=280&height=200 "doc") ![Load](http://lcas.lincoln.ac.uk/jenkins/label/doc/loadStatistics/graph?type=min&width=280&height=200 "doc") ![Load](http://lcas.lincoln.ac.uk/jenkins/label/doc/loadStatistics/graph?type=hour&width=280&height=200 "doc") 
