add_example(ConvertSpatialObjectToImage)
compare_to_baseline(EXAMPLE_NAME ConvertSpatialObjectToImage
  BASELINE_PREFIX ConvertSpatialObjectToImage
  )

add_example(Ellipse)
compare_to_baseline(EXAMPLE_NAME Ellipse
  BASELINE_PREFIX EllipseOutput
  )

add_example(LineSpatialObject)
compare_to_baseline(EXAMPLE_NAME LineSpatialObject
  BASELINE_PREFIX line
  )

add_example(Blob)

if(ENABLE_QUICKVIEW)

add_example(ContourSpatialObject)

endif()