class Constants:
    yaml_file = "E:\\A\\TransportSystem\\src\\main\\resources\\settings.yaml"

    class YamlNames:
        app = "app"
        initTransportSystemFiles = "initTransportSystemFiles"

    class JsonNames:
        file_name = "file_name"
        flow = "flow"
        input_data_paths = "input_data_paths"
        load_period = "load_period"
        model_parameters = "model_parameters"
        output_data_path = "output_data_path"
        output_data_paths = "output_data_paths"
        path = "path"
        plot_name = "plot_name"
        plot_type = "plot_type"
        time = "time"


        # If pi2_criterion is True, filter the dataset to include only rows
        # where the 'time' value is less than the specified 'max_time_value'.
        # This is used to limit the data range for further calculations or analysis.
        pi2_criterion = "pi2_criterion"

        # Maximum time value used to limit the data range for analysis.
        # Only entries with time < max_time_value are considered.
        max_time_value ="max_time_value"

        plot_parameters = "plot_parameters"
        plot_template = "plot_template"
        plot_structure = "plot_structure"
        x_column = "x_column"
        y_columns = "y_columns"

