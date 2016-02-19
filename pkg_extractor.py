import zipfile
import os
import sys
from xml.dom import minidom

def unzip(source_filename, dest_dir):
    try:
        print "[*] Unzipping Files from %s to %s" %(source_filename, dest_dir)
        with zipfile.ZipFile(source_filename) as zf:
            zf.extractall(dest_dir)

    except Exception as e:
        print "[ERROR] Unzipping Files from %s to %s" %(source_filename, dest_dir) + str(e)

def list_dirfiles(dest_dir):
    try:
        print "\n[*] Listing Files and Directories from %s" %source_filename
        for path, subdir, files in os.walk(dest_dir):
            for name in files:
                print os.path.join(path, name)
                if ('/' not in path[len(dest_dir):]) and (name.endswith('.xml')):
                    xml_file = os.path.join(path, name)
        parse_xml(xml_file)
            
    except Exception as e:
            print "[ERROR] Listing Files and Directories from %s" %source_filename + str(e)

def parse_xml(file_name):
    try:
        print "\n[*] Parsing %s file" %file_name
        dom = minidom.parse(file_name)
        print "SupportedOS:"
        print "ID"
        for node in dom.getElementsByTagName('supportedOS'):
            print node.getAttribute("Id")
        print "\nAssembly Identity:"
        print "Name ---- Version ---- Public Key Token"
        for node in dom.getElementsByTagName('assemblyIdentity'):
            print node.getAttribute("name") + " ----",
            print node.getAttribute("version") + " ----",
            print node.getAttribute("publicKeyToken")
            
    except Exception as e:
        print "[ERROR] Parsing %s files" %file_name + str(e)

if __name__ == "__main__":
    source_filename = sys.argv[1]
    dest_dir = sys.argv[2]
    unzip(source_filename, dest_dir)
    list_dirfiles(dest_dir)
    print "\n[*] Successfully Completed"
