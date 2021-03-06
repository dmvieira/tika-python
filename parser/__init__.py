import tika

def from_file(filename):
    """Parse filename using tika's AutoDetectParser."""
    stream = tika.FileInputStream(tika.File(filename))
    return __parse(stream)

def from_buffer(string):
    """Parse raw binary string using tika's AutoDetectParser."""
    stream = tika.ByteArrayInputStream(tika.JArray_byte(string))
    return __parse(stream)

def to_xml_from_file(filename):
    """Parse content from a file and return back XHTML representation"""
    stream = tika.FileInputStream(tika.File(filename))
    return __handler(stream)

def to_xml_from_string(string):
    """Parse content from a string and return back XHTML representation"""
    stream = tika.ByteArrayInputStream(tika.JArray_byte(string))
    return __handler(stream)

def __handler(stream):
    handler = tika.ToHTMLContentHandler()
    met = tika.Metadata()
    pc = tika.ParseContext()
    parser = tika.AutoDetectParser()
    parser.parse(stream, handler, met, pc)
    return handler.toString()

def __parse(stream):
    parsed = {}
    parser = tika.AutoDetectParser()
    content = tika.BodyContentHandler(-1)
    metadata = tika.Metadata()
    context = tika.ParseContext()
    parser.parse(stream, content, metadata, context)
    parsed["content"] = content.toString()
    parsed["metadata"] = {}
    for n in metadata.names():
        parsed["metadata"][n] = metadata.get(n)
    return parsed
