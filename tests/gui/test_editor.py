# ###################################################
# Copyright (C) 2012 The Unknown Horizons Team
# team@unknown-horizons.org
# This file is part of Unknown Horizons.
#
# Unknown Horizons is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

from tests.gui import gui_test


@gui_test(additional_cmdline=["--edit-map", "development"])
def test_place_tiles(gui):
	"""Place different tiles with different tile sizes."""

	gui.trigger('editor_settings', 'water')
	gui.cursor_click(27, 36, 'left')
	gui.cursor_click(27, 37, 'left')
	gui.cursor_click(27, 38, 'left')

	gui.trigger('editor_settings', 'size_2')
	gui.trigger('editor_settings', 'sand')
	gui.cursor_click(34, 34, 'left')

	gui.trigger('editor_settings', 'size_3')
	gui.trigger('editor_settings', 'default_land')
	gui.cursor_click(34, 27, 'left')