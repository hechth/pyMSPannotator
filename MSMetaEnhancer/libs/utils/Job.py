from MSMetaEnhancer.libs.utils.Errors import ConversionNotSupported, SourceAttributeNotAvailable


class Job:
    def __init__(self, data):
        self.source, self.target, self.converter = data

    def __str__(self):
        return f'{self.converter}: {self.source} -> {self.target}'

    def __repr__(self):
        return f'Job(({self.source}, {self.target}, {self.converter}))'

    def validate(self, converters, metadata):
        """
        Makes sure to job is supported or possible to execute on given metadata.

        :param converters: available endpoints
        :param metadata: given metadata
        :return: particular converter and data if conversion is possible
        """
        converter = converters.get(self.converter, None)
        data = metadata.get(self.source, None)

        if converter is None:
            raise ConversionNotSupported(f'Conversion ({self.converter}) {self.source} -> {self.target}: '
                                         f'is not supported')
        elif data is None:
            raise SourceAttributeNotAvailable(f'Conversion ({self.converter}) {self.source} -> {self.target}: '
                                              f'Attribute {self.source} missing in given metadata.')
        else:
            return converter, data


def convert_to_jobs(jobs):
    return [Job(data) for data in jobs]
