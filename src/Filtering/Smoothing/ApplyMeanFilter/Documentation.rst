Mean Filtering Of An Image
============================

.. index::
   single: MeanImageFilter
   single: smooth

Synopsis
--------

Apply mean filtering on an image.


Results
-------

.. figure:: Gourds.png
  :alt: Input image

  Input image

.. figure:: OutputBaseline.png
  :alt: Output image

  Output image


Code
----

C++
...

.. literalinclude:: Code.cxx
   :lines: 18-

Python
......

.. literalinclude:: Code.py
   :language: python
   :lines: 1, 16-

Classes demonstrated
--------------------

.. breathelink:: itk::MeanImageFilter
