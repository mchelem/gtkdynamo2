#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mydialog.py
#
#  Copyright 2014 Fernando Bachega <fernando@bachega>
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
#
import os
import gtk
import gobject
from pDynamoMethods.pDynamoCharges   import rescale_charges


class ChargeRescaleDialog():
    def  on_button_rescale_charges_clicked(self, button):
        """ Function doc """
        selection       = self.builder.get_object    ('entry_pymol_selection').get_text()
        total_charge    = int(self.builder.get_object('entry_charge').get_text())
        print 'selection:', selection, '\ntotal charge:',total_charge
        
        try:
            rescale_charges(self.project, selection, total_charge)
        except:
            print 'Charge rescaling error!'
        
        
        
    def __init__(self, GTKDynamoSession = None):
        """ Class initialiser """
        self.builder          = gtk.Builder()
        
        if GTKDynamoSession != None:
            self.project          = GTKDynamoSession.project
            self.main_builder     = GTKDynamoSession.builder
            self.GTKDynamoSession = GTKDynamoSession        
            self.window_control   = GTKDynamoSession.window_control
            self.GTKDYNAMO_ROOT   = GTKDynamoSession.GTKDYNAMO_ROOT
            self.GTKDYNAMO_GUI    = GTKDynamoSession.GTKDYNAMO_GUI 
        
        else:
            self.GTKDYNAMO_ROOT = ''
            self.GTKDYNAMO_GUI  = ''       


        self.builder.add_from_file(
            os.path.join(self.GTKDYNAMO_GUI, 'ChargeRescale.glade'))
        self.builder.connect_signals(self)
        self.dialog = self.builder.get_object('dialog_charge_rescale')

        #'''
		#--------------------------------------------------
		#-                                                -
		#-	              WindowControl                  -
		#-                                                -
		#--------------------------------------------------
		#'''
        #self.window_control = WindowControl(self.builder)
        #
        ##----------------- Setup ComboBoxes -------------------------#
        #combobox = 'combobox1_nb_types'         #
        #combolist = nbList
        #self.window_control.SETUP_COMBOBOXES(combobox, combolist, 0)
        ##------------------------------------------------------------#


def main():
    dialog = ChargeRescaleDialog()
    dialog.dialog.run()
    dialog.dialog.hide()
if __name__ == '__main__':
    main()