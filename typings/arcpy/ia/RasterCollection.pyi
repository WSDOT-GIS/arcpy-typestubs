"""
This type stub file was generated by pyright.
"""

class _RasterCollectionCursor:
    def __init__(self, data_frame) -> None:
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self): # -> Self@_RasterCollectionCursor:
        ...
    
    def __next__(self):
        ...
    


class RasterCollection:
    def __init__(self, rasters, attribute_dict=..., where_clause=..., query_geometry=...) -> None:
        ...
    
    def filter(self, where_clause=..., query_geometry_or_extent=..., raster_query=...): # -> RasterCollection | None:
        """
        filter a raster collection based on attribute and/or spatial queries

        :param where_clause (SQL Expression): An SQL expression used to select a subset of rasters
        :param query_geometry_or_extent (feature, feature layer, raster dataset, raster layer, extent, geometry): items in the collection that fails to intersect the given geometry will be excluded
        :param raster_query (SQL Expression): An SQL expression used to select a subset of rasters by the raster's key properties
        :return(RaterCollection): a raster collection that only contains items sastisfying the queries
        """
        ...
    
    @property
    def fields(self): # -> list[Unknown] | Any:
        ...
    
    @property
    def count(self): # -> int:
        ...
    
    def __iter__(self): # -> _RasterCollectionCursor:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __getitem__(self, item):
        ...
    
    def filterByTime(self, start_time=..., end_time=..., time_field_name=..., date_time_format=...): # -> Self@RasterCollection | RasterCollection | None:
        """
        Shortcut to filter a collection by time

        :param start_time(String): a string representation of the start time, format must be '%m/%d/%Y', i.e., '10/03/2019'
        :param end_time(String): a string representation of the end time. format must be '%m/%d/%Y', i.e., '10/03/2019'.
                                This is optional. If not provided, only items that have exactly same time value as the start_time would be inlucded in the output
        :param time_field_name(String): the name of the field containing the time information for each item. Default: "StdTime"
        :param date_time_field(String): default is None which uses the default string representation of arcgis date field type
                                        if default is used, the date_time_format means '%Y-%m-%dT%H:%M:%S'
        :param date_time_format(String): the time format that is used to format the time field values. Please ref the python
                                date time standard for this argument. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
                                Default is None and this means using the Pro standard time format '%Y-%m-%dT%H:%M:%S'
                                and ignoring the following sub-second.

        :return(RaterCollection): a filtered raster collection.
        """
        ...
    
    def filterByGeometry(self, query_geometry_or_extent=...): # -> RasterCollection | None:
        """
        Shortcut to filter a collection by geometries. Only those items that have intersection with the given geometry would be kept in the output

        :param query_geometry_or_extent (feature, feature layer, raster dataset, raster layer, extent, geometry): items in the collection that fails to intersect the given geometry will be excluded
        :return(RaterCollection): a filtered raster collection
        """
        ...
    
    def filterByAttribute(self, field_name, operator, field_values): # -> RasterCollection | None:
        """
        Shortcut to filter a collection by attribute

        :param field_name(String): the name of the field to filter
        :param operator(String): one of "EQUALS", "LESS_THAN", "GREATER_THAN","NOT_EQUALS", "NOT_LESS_THAN", "NOT_GREATER_THAN",
                        "STARTS_WITH", "ENDS_WITH", "NOT_STARTS_WITH", "NOT_ENDS_WITH", "CONTAINS", "NOT_CONTAINS",
                        "IN" and "NOT_IN"
        :param field_values (String, Numeric, List): the values to compare against.
        :return(RaterCollection): a filtered raster collection
        """
        ...
    
    def sort(self, field_name, ascending=...): # -> RasterCollection:
        """
        sort a raster collection by the specified field name

        :param field_name (String): the field to sort by
        :param ascending (Bool): Whether to sort in ascending or descending order. Default: true (ascending)
        :return(RaterCollection): a sorted raster collection
        """
        ...
    
    def getFieldValues(self, field_name, max_count=...): # -> list[Unknown] | Any:
        """
        get values of a given field
        :param field_name (String): the field name to extract values from
        :param max_count (Int): the number to limit the collection to.
        :return(RaterCollection): a list of values at the given field
        """
        ...
    
    def toMultidimensionalRaster(self, variable_field_name=..., dimension_field_names=...):
        """
        convert the raster collection to a multidimensional raster

        :param variable_field_name (String): the name of the field that contains the variable names
        :param dimension_field_names (String, List of String): the name(s) of the fields that contains the dimension names
        :return(Raster): a multidimensional raster. Each item in the source raster collection becomes a slice in the multidimensional raster
        """
        ...
    
    def max(self, ignore_nodata=..., extent_type=..., cellsize_type=...):
        """
        For each band, calculate the maximum value of each pixel across the the stack of rasters. Bands are matched by band index

        :param ignore_nodata (Bool): Specifies whether NoData values are ignored.

                                    - True : The method will include all valid pixels and ignore any NoData pixels.
                                                This is the default.
                                    - False : The method will result in NoData if there are any NoData values.
        :param extent_type(string): one of "FirstOf", "IntersectionOf" "UnionOf", "LastOf"
        :param cellsize_type(string): one of "FirstOf", "MinOf", "MaxOf "MeanOf", "LastOf"
        :return(Raster): a raster that contains the maximum value of each pixel at each band
        """
        ...
    
    def min(self, ignore_nodata=..., extent_type=..., cellsize_type=...):
        """
        For each band, calculate the minimum value of each pixel across the the stack of rasters. Bands are matched by band index
        :param ignore_nodata (Bool): Specifies whether NoData values are ignored.

                                    - True : The method will include all valid pixels and ignore any NoData pixels.
                                                This is the default.
                                    - False : The method will result in NoData if there are any NoData values.
        :param extent_type(string): one of "FirstOf", "IntersectionOf" "UnionOf", "LastOf"
        :param cellsize_type(string): one of "FirstOf", "MinOf", "MaxOf "MeanOf", "LastOf"
        :return(Raster): a raster that contains the minimum value of each pixel at each band
        """
        ...
    
    def median(self, ignore_nodata=..., extent_type=..., cellsize_type=...):
        """
        For each band, calculate the median value of each pixel across the the stack of rasters. Bands are matched by band index

        :param ignore_nodata (Bool): Specifies whether NoData values are ignored.

                                    - True : The method will include all valid pixels and ignore any NoData pixels.
                                                This is the default.
                                    - False : The method will result in NoData if there are any NoData values.
        :param extent_type(string): one of "FirstOf", "IntersectionOf" "UnionOf", "LastOf"
        :param cellsize_type(string): one of "FirstOf", "MinOf", "MaxOf "MeanOf", "LastOf"
        :return(Raster): a raster that contains the median value of each pixel at each band
        """
        ...
    
    def mean(self, ignore_nodata=..., extent_type=..., cellsize_type=...):
        """
        For each band, calculate the mean value of each pixel across the the stack of rasters. Bands are matched by band index

        :param ignore_nodata (Bool): Specifies whether NoData values are ignored.

                                    - True : The method will include all valid pixels and ignore any NoData pixels.
                                                This is the default.
                                    - False : The method will result in NoData if there are any NoData values.
        :param extent_type(string): one of "FirstOf", "IntersectionOf" "UnionOf", "LastOf"
        :param cellsize_type(string): one of "FirstOf", "MinOf", "MaxOf "MeanOf", "LastOf"
        :return(Raster): a raster that contains the mean value of each pixel at each band
        """
        ...
    
    def majority(self, ignore_nodata=..., extent_type=..., cellsize_type=...):
        """
        For each band, calculate the majority value of each pixel across the the stack of rasters. Bands are matched by band index

        :param ignore_nodata (Bool): Specifies whether NoData values are ignored.

                                    - True : The method will include all valid pixels and ignore any NoData pixels.
                                                This is the default.
                                    - False : The method will result in NoData if there are any NoData values.
        :param extent_type(string): one of "FirstOf", "IntersectionOf" "UnionOf", "LastOf"
        :param cellsize_type(string): one of "FirstOf", "MinOf", "MaxOf "MeanOf", "LastOf"
        :return(Raster): a raster that contains the majority value of each pixel at each band
        """
        ...
    
    def sum(self, ignore_nodata=..., extent_type=..., cellsize_type=...):
        """
        For each band, calculate the sum value of each pixel across the the stack of rasters. Bands are matched by band index

        :param ignore_nodata (Bool): Specifies whether NoData values are ignored.

                                    - True : The method will include all valid pixels and ignore any NoData pixels.
                                                This is the default.
                                    - False : The method will result in NoData if there are any NoData values.
        :param extent_type(string): one of "FirstOf", "IntersectionOf" "UnionOf", "LastOf"
        :param cellsize_type(string): one of "FirstOf", "MinOf", "MaxOf "MeanOf", "LastOf"
        :return(Raster): a raster that contains the sum value of each pixel at each band
        """
        ...
    
    def std(self, ignore_nodata=..., extent_type=..., cellsize_type=...):
        """
        For each band, calculate standard deviation of each pixel across the the stack of rasters. Bands are matched by band index

        :param ignore_nodata (Bool): Specifies whether NoData values are ignored.

                                    - True : The method will include all valid pixels and ignore any NoData pixels.
                                                This is the default.
                                    - False : The method will result in NoData if there are any NoData values.
        :param extent_type(string): one of "FirstOf", "IntersectionOf" "UnionOf", "LastOf"
        :param cellsize_type(string): one of "FirstOf", "MinOf", "MaxOf "MeanOf", "LastOf"
        :return(Raster): a raster that contains the sum value of each pixel at each band
        """
        ...
    
    def mosaic(self, mosaic_method=...):
        """
        Composites all the rasters in a collection to a single raster

        :param mosaic_method (String): the method used to handle overlapping areas, including FIRST(default),'LAST', 'MIN', 'MAX', 'MEAN', 'MEDIAN', 'SUM'
        :return(Raster): a raster after mosaicing all the rasters in the collection
        """
        ...
    
    def qualityMosaic(self, quality_rc_or_list, statistic_type=...):
        """
        Composites all the rasters in a collection based on a quality input. By default, each pixel in the output is based on which image in the collection has the same index with the image in the quality_rc_or_list that has the maximum value (default)

        :param quality_rc_or_list(RasterCollection or List): the raster colltion or a list of Raster to be used as quality. It must have same number of items with the collection to be mosaiced.
        :param statistic_type(String): the statistic method used to get the index from the quality rc. Its value could be MAX(default),MIN, MEDIAN
        :return(Raster): a raster after mosaicing all the rasters in the collection
        """
        ...
    
    def selectBands(self, band_ids_or_names): # -> RasterCollection:
        """
        Return a new raster collection that only contains the selected bands in each raster

        :param band_ids_or_names (List): a list of Band ID or Band Names. Band ID uses one-based indexing
        :return(RasterCollection): a raster collection with only the selected bands
        """
        ...
    
    def map(self, func): # -> RasterCollection:
        """
        apply a function to each item in the raster collection
        :param func: follows the signature:
                    Args: item, an item in the raster collection
                    Returns: dict, {'raster': arcpy.Raster, fieldName:fieldValue ...}
        :return:
            a new raster collection object that has applied the func to each item
        """
        ...
    
    def filterByRasterProperty(self, property_name, operator, property_values):
        """
        filter the raster collection by property of each raster

        :param property_name: str, the property name to operate on
        :param operator: "EQUALS", "LESS_THAN", "GREATER_THAN","NOT_EQUALS", "NOT_LESS_THAN", "NOT_GREATER_THAN",
                        "STARTS_WITH", "ENDS_WITH", "NOT_STARTS_WITH", "NOT_ENDS_WITH", "CONTAINS", "NOT_CONTAINS",
                        "IN" and "NOT_IN"
        :param property_values: String or List of String
        :return: filtered RasterCollection or None if no raster is selected
        """
        ...
    
    def filterByCalendarRange(self, calendar_field, start, end=..., time_field_name=..., date_time_format=...):
        """
        filter the raster collection by a calindar_field and its start and end value (inclusive). i.e. if you would like
        to select all the rasters that have the time stamp on Monday, specify calendar_field as 'DAY_OF_WEEK' and put start and
        end to 1.

        :param calendar_field: string, one of 'YEAR', 'MONTH', 'QUARTER', 'WEEK_OF_YEAR', 'DAY_OF_YEAR', 'DAY_OF_MONTH',
         'DAY_OF_WEEK', 'HOUR'
        :param start: integer, the start time. inclusive.
        :param end: integer, default is None, if default is used, the end is set equal to start. inclusive.
        :param time_field_name: string, the time field anme, default is 'StdTime'.
        :param date_time_format: the time format that is used to format the time field values. Please ref the python
                                date time standard for this argument. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
                                Default is None and this means using the Pro standard time format '%Y-%m-%dT%H:%M:%S'
                                and ignoring the following sub-second.

        :return: a filtered raster collection.
        """
        ...
    
    def summarizeField(self, field_name, summary_type=...):
        """
        Summarizes a numeric field of the RasterCollection based on the specified summary_type
        :param field_name: str, the field name to be summarized
        :param summary_type: str or list of str representing the summary type."COUNT", "COUNT_DISTINCT", "FIRST","HISTOGRAM", "MAX", "MEAN", "MIN",
                        "PRODUCT", "SAMPLE_SD", "SAMPLE_VAR", "SUM", "TOTAL_SD", "TOTAL_VAR", "ALL".
        :return: a dictionary with key being the summary type and the value being the summary value.
        """
        ...
    
    def merge(self, collection2): # -> RasterCollection:
        """
         merge method merges two image collections into one. The output has all the items that were in either collection.
        :param collection2: RasterCollection object. The second collection to merge.
        :return: Collection that has all the items that were in either collection.
        """
        ...
    
    def reduce(self, func, func_args=...):
        """
        The ``reduce`` method composite all the images in the collection to a single image based on a reducer function. 

        :param func: The Python function to reduce the raster collection. 
                     The function should accept a list of rasters as first parameter and return a single raster
        :param func_args: Optional dictionary. Additional paramters to be passed the reducer function.
        :return: Returns what the the function specified in the func arg returns

        .. code-block:: python

            # Usage Example 1: This snippet reduces a raster collection based on a reducer function from arcpy.ia module that can accept a list of rasters

            rc = RasterCollection("<data path>")
            from arcpy.ia import Max
            max_raster = rc.reduce(func=Max, func_args={"extent_type":"UnionOf"})


            # Usage Example 2: This snippet reduces a raster collection based on a custom reducer function.

            rc = RasterCollection("<data path>")

            def skewness(ras_list):
                from arcpy.ia import CellStatistics, Power, Plus
                cs_mean = CellStatistics(ras_list, "MEAN", process_as_multiband="MULTI_BAND")
                cs_stddev  = CellStatistics(ras_list, "STD", process_as_multiband="MULTI_BAND")
                cs_median = CellStatistics(ras_list, "MEDIAN", process_as_multiband="MULTI_BAND")
                out_skewness = 3*(cs_mean - cs_median)/cs_stddev
                return out_skewness

            skewness = rc.reduce(func=skewness)

        """
        ...
    
    def addField(self, field_name, field_values): # -> RasterCollection:
        """
         Adds a new field to the raster collection and populate it with values.
        :param field_name: Required string. The name of the field to be added. 
        :param field_values: Required list. The list of values associated with the field name. 
                             The length of the list should match the number of items in the raster collection
                             Providing only one value will set the same value for all rows. 
        :return: Collection that has the new field added.
        """
        ...
    
    def groupBy(self, field_name): # -> dict[Unknown, Unknown]:
        """
         groupBy method can be used to group the raster collection based on a field.
        :param field_name: Required string.The name of the field that is used to group the raster collection. Items with the same field values will be grouped together. 
        :return: Dictionary.The dictionary that contains the grouped raster collections. The key of the dictionary is a field value of the field name that the grouping is based on. 
                 The value of the dictionary is a raster collection whose field name contains the same field value.
        """
        ...
    


