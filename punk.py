from pyforms 			import BaseWidget
from pyforms.Controls 	import ControlBoundingSlider
from pyforms.Controls 	import ControlText
from pyforms.Controls 	import ControlButton
from pyforms.Controls 	import ControlCheckBox
from pyforms.Controls 	import ControlCheckBoxList
from pyforms.Controls 	import ControlCombo
from pyforms.Controls 	import ControlDir
from pyforms.Controls 	import ControlDockWidget
from pyforms.Controls 	import ControlEmptyWidget
from pyforms.Controls 	import ControlFile
from pyforms.Controls 	import ControlFilesTree
from pyforms.Controls 	import ControlImage
from pyforms.Controls 	import ControlList
from pyforms.Controls 	import ControlPlayer
from pyforms.Controls 	import ControlProgress
from pyforms.Controls 	import ControlSlider
from pyforms.Controls 	import ControlVisVis
from pyforms.Controls 	import ControlVisVisVolume
from pyforms.Controls 	import ControlEventTimeline

import pyforms
import numpy as np


class Example3(BaseWidget):

	def __init__(self):
		super(Example3,self).__init__('Simple example 1')

		#Definition of the forms fields
		self._combobox 		= ControlCombo('Choose a item')
		self._list 			= ControlList('List label')
		self._progress 		= ControlProgress('Progress bar')
		# self._visvisVolume	= ControlVisVisVolume('Visvis')
		self._timeline 		= ControlEventTimeline('Timeline')


		self.formset = [ ('_combobox',' '), '_progress', '=',('_visvisVolume', '||','_list'), '_timeline']


		# self._combobox.addItem('Item 1', 'Value 1')
		# self._combobox.addItem('Item 2', 'Value 2')
		# self._combobox.addItem('Item 3', 'Value 3')
		# self._combobox.addItem('Item 4') #The value is = to the item

		self._list.value = [ ('Item1', 'Item2', 'Item3',), ('Item3', 'Item4', 'Item5',)]

		#Create a an example of an image with volume
		# imageWithVolume 	= np.zeros( (100,100,100), np.uint8 )
		# imageWithVolume[30:40, 30:50, :] = 255
		# imageWithVolume[30:40, 70:72, :] = 255
		#############################################

		# self._visvisVolume.value = imageWithVolume

##################################################################################################################
##################################################################################################################
##################################################################################################################

#Execute the application
if __name__ == "__main__": pyforms.start_app( Example3 )