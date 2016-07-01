import jinja2
import os
import sys
import xml.etree.ElementTree as ET

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
jinja_file = "Docs.jinja"
xml_file = "classMotor.xml"


class DocGen:
    def __init__(self, jinja_file):
        self.template = JINJA_ENVIRONMENT.get_template(jinja_file)
    def generate(self, xml):
        # Everything interesting is nested within compounddef
        class_info = ET.parse( xml ).getroot().find("compounddef") 
        class_name = class_info.find("compoundname")
        public_funcs = [ c for c in class_info.findall("sectiondef") if c.attrib["kind"] == "public-func" ][0]
        function_list = []
        for f in public_funcs:
            info_tuple = []
            name = f.find("name").text
            type = f.find("type").text
            args = f.find("argsstring").text
            # If we're dealing with the constructor, then this field will be None
            if type is None: type = "" 
            else: type = type + " "
            desc = f.find("detaileddescription").find("para") 
            # Process the description
            if desc is not None: desc = desc.text
            else: desc = ""
            info_tuple.append( type+name+args )
            info_tuple.append( desc )
            function_list.append(info_tuple)
        jinja_vars = {"class_name" : class_name.text,
                      "function_list" : function_list}
        return self.template.render(jinja_vars).encode('ascii', 'ignore')

if __name__ == "__main__":
    out_file = open("test.html", "w")
    out_file.write(DocGen(jinja_file).generate(xml_file))