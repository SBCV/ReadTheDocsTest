..
   Blender-Addon-Photgrammetry-Importer documentation master file, created by
   sphinx-quickstart on Sat Jun 20 18:28:02 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

####################################
Blender-Addon-Photgrammetry-Importer 
####################################

.. 
   https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html
      Heading Levels (recommended order)
         # with overline
         * with overline
         =
         -
         ^
         "
   There should be only one H1 in a document.

This documentation describes an `addon for Blender <https://github.com/SBCV/Blender-Addon-Photogrammetry-Importer>`_ that allows to import different reconstruction results of several :code:`Structure from Motion` and :code:`Multi-View Stereo` libraries.

Supported libraries (data formats):

.. hlist::
   :columns: 1

   - `Colmap <https://github.com/colmap/colmap>`_ (Model folders (BIN and TXT), workspaces, NVM, PLY) 
   - `Meshroom <https://alicevision.github.io/>`_ (MG, JSON, SfM, PLY)
   - `MVE <https://github.com/simonfuhrmann/mve>`_ (MVE workspaces) :sup:`1`
   - `Open3D <http://www.open3d.org/>`_ (JSON, LOG, PLY) :sup:`1`
   - `OpenSfM <https://github.com/mapillary/OpenSfM>`_ (JSON)
   - `OpenMVG <https://github.com/openMVG/openMVG>`_ (JSON, NVM, PLY) :sup:`2`
   - `Regard3D <https://www.regard3d.org/>`_ (OpenMVG JSON)
   - `VisualSFM <http://ccwu.me/vsfm/>`_ (NVM) :sup:`1`

In addition, the addon supports some common point cloud data formats:

.. hlist::
   :columns: 1

   - `Polygon files <http://paulbourke.net/dataformats/ply/>`_ (PLY) :sup:`3`
   - `Point Cloud Library files <https://github.com/PointCloudLibrary/pcl>`_ (PCD) :sup:`3`
   - `LASer files <https://www.asprs.org/divisions-committees/lidar-division/laser-las-file-format-exchange-activities>`_ (LAS) :sup:`3, 4`
   - `LASzip files <https://laszip.org/>`_ (LAZ) :sup:`3, 4, 5`
   - `Simple ASCII point files <https://www.cloudcompare.org/doc/wiki/index.php?title=FILE_I/O>`_ (ASC, PTS, CSV) :sup:`3`

| :sup:`1` Requires :code:`pillow` to read image sizes from disk. :sup:`2` Requires :code:`pillow` for point color computation.
| :sup:`3` Requires :code:`pyntcloud` for parsing. :sup:`4` Requires :code:`laspy` for parsing. :sup:`5` Requires :code:`lazrs` for parsing.

The latest release of the addon is currently compatible with Blender 3.1.2 onwards. 
For older Blender versions you might find a suitable release `here <https://github.com/SBCV/Blender-Addon-Photogrammetry-Importer/releases>`_.