#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pDynamoMinimization.py
#
#  Copyright 2014 Labio <labio@labio-XPS-8300>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import os
import time
#import sys

# pDynamo
from pBabel import *
from pCore import *
from pMolecule import *
from pMoleculeScripts import *

from DualTextLogFileWriter3 import *
from pprint import pprint

EasyHybrid_ROOT = os.getcwd()
PDYNAMO_SCRATCH = os.environ.get('PDYNAMO_SCRATCH')


EasyHybrid_TMP = os.path.join(PDYNAMO_SCRATCH, '.EasyHybrid')
if not os.path.isdir(EasyHybrid_TMP):
    os.mkdir(EasyHybrid_TMP)
    print "Temporary files directory:  %s" % EasyHybrid_TMP


def pDynamoTrajectoryEnergyRefine (system=None, data_path=None, trajectory = None, _type = '1D'):

                               # Local time  -  LogFileName 
    #----------------------------------------------------------------------------------------
    localtime = time.asctime(time.localtime(time.time()))                                    
    localtime = localtime.split()                                                            
    #  0     1    2       3         4                                                        
    #[Sun] [Sep] [28] [02:32:04] [2014]                                                      
    LogFile = 'Energy_' + localtime[1] +'_' + localtime[2] + '_'+localtime[3]+'_' + localtime[4]+'.log'       #
    #----------------------------------------------------------------------------------------
    log = DualTextLog(data_path, LogFile)  # LOG

    #--------------------#
    #    Initial time    #
    #--------------------#
    t_initial = time.time()

    #---------------------------------#
    #             SUMMARY             #
    #---------------------------------#
    
    if _type == '1D':
        system.Summary(log=log)
        energy_table  = []
        
        trajectory = SystemGeometryTrajectory (trajectory, system, mode = "r" )

        n = 0 
        while trajectory.RestoreOwnerData ( ):
            energy = system.Energy(log=log)
            dipolo = system.DipoleMoment ()
            energy_table.append(energy)
            n  += 1

        pprint (energy_table)

    
    if _type == '2D':

        #--------------------------------------------------------------#
        trajectory_files   = os.listdir(parameters['trajectory'])      #
        trajectory_files2  = []                                        #
        #--------------------------------------------------------------#
        for File in trajectory_files:                                  #
            File2 = File.split('.')                                    #
                                                                       #
            if File2[-1] == 'pkl':                                     #
                trajectory_files2.append(File)                         #
        #--------------------------------------------------------------#


        for File in  trajectory_files2:
            print File


        #system.Summary(log=log)
        #energy_table  = []
        #
        #trajectory = SystemGeometryTrajectory (trajectory, system, mode = "r" )
        #
        #n = 0 
        #while trajectory.RestoreOwnerData ( ):
        #    energy = system.Energy(log=log)
        #    dipolo = system.DipoleMoment ()
        #    energy_table.append(energy)
        #    n  += 1
        #
        #pprint (energy_table)




    else: 
        print '_type =  UNK'
    
    #back_orca_output(output_path, step)

    #--------------------#
    #     final time     #
    #--------------------#      
    t_final = time.time()
    total_time  = t_final - t_initial
    print "Total time = : ", t_final - t_initial
    return energy


def main():
    system = Unpickle(EasyHybrid_ROOT + '/test/test.pkl')
    _min_ = pDynamoEnergy(system)
    #_min_    = pDynamoMinimization(system,'Steepest Descent')
    #_min_    = pDynamoMinimization(system,'LBFGS')
    return 0

if __name__ == '__main__':
    main()
