#!/usr/bin/env python

# Copyright NumFOCUS
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import itk

if len(sys.argv) != 2:
    print('Usage: ' + sys.argv[0] + ' <OutputFileName>')
    sys.exit(1)

Dimension = 2

PixelType = itk.UC

OutputFileName = sys.argv[1]

ImageType = itk.Image[PixelType, Dimension]

region = itk.ImageRegion[Dimension]()

start = itk.Index[Dimension]()
start.Fill(0)

region.SetIndex(start)

size = itk.Size[Dimension]()
size[0] = 200
size[1] = 300

region.SetSize(size)

image = ImageType.New()
image.SetRegions(region)
image.Allocate()
image.FillBuffer(itk.NumericTraits[PixelType].ZeroValue())

pixelIndex = itk.Index[Dimension]()

for r in range(50):
    pixelIndex[0] = 4 * r
    pixelIndex[1] = 4 * r

    image.SetPixel(pixelIndex, 128)

    pixelIndex[0] = 4 * r
    pixelIndex[1] = 200 - 4 * r

    image.SetPixel(pixelIndex, 255)

for r in range(25):
    pixelIndex[0] = 8 * r
    pixelIndex[1] = 200 + 4 * r

    image.SetPixel(pixelIndex, 128)

    pixelIndex[0] = 8 * r
    pixelIndex[1] = 250

    image.SetPixel(pixelIndex, 180)

pixelIndex[0] = 95
pixelIndex[1] = 150

image.SetPixel(pixelIndex, 200)

pixelIndex[0] = 100
pixelIndex[1] = 150

image.SetPixel(pixelIndex, 200)

pixelIndex[0] = 105
pixelIndex[1] = 150

image.SetPixel(pixelIndex, 200)

pixelIndex[0] = 100
pixelIndex[1] = 155

image.SetPixel(pixelIndex, 200)

pixelIndex[0] = 100
pixelIndex[1] = 145

image.SetPixel(pixelIndex, 200)

itk.imwrite(image, OutputFileName)
