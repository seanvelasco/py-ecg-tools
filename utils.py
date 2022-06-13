from lxml import etree
import unicodedata

dashlabs_metadata = """
<metadata>
    <title>Dashlabs.ai</title>
    <description>We are a DIY end-to-end lab software company. We focus on small and mid-sized labs to accelerate access to quality healthcare for everyone.</description>
</metadata>
"""

dashlabs_metadata_dev = """
<metadata>
    <title>hello LSD from RIM :D</title>
    <description>this svg can be printed on paper as is</description>
    <description>vector should not be scaled up or down</description>
    <description>1 grid === 5 mm on paper</description>
    <description>width is 27.5 cm (5mm * 55 blocks (0s to 11s))</description>
    <description>height is 48 cm (0.5 mV * 8 blocks (-2mV to 2mV) * 12 leads)</description>
    <description>this msg is shown if chart is generated in dev</description>
</metadata>
"""

def sanitize_xml(xml):
    svg_string = unicodedata.normalize('NFKD', xml.getvalue()).encode('utf-8', 'ignore')
    doc = etree.fromstring(svg_string)
    
    for element in doc.iter("{http://www.w3.org/2000/svg}metadata"):
        doc.remove(element)
    
    metadata = etree.fromstring(dashlabs_metadata)
    doc.insert(0, metadata)
    
    svg_string = etree.tostring(doc, encoding='unicode')
        
    return svg_string