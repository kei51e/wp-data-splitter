# wp-data-splitter.py: split a large wordpress export file into smaller ones
# See https://github.com/kei-51/wp-data-splitter for usage and license. 

import sys

def main():

  # 1.5M char counts as default since 2M bytes is the popular PHP upload limit.
  limit = 1572864

  if len(sys.argv) == 2:
    file = sys.argv[1]
  elif len(sys.argv) == 3:
    file = sys.argv[1]
    if sys.argv[2].isdigit() == False:
      print "wp_data_splitter.py <filename> <limit size in byte>"
      sys.exit()
    limit = int(sys.argv[2])
  else:
    print "wp_export_splitter.py <filename>"
    sys.exit()

  # set the internal limit not to exceed the hard limit
  limit -= 10000

  src = open(file,'r')

  header = read_header(src)
  header_wc = header.count('')

  footer = '</channel></rss>'
  footer_wc = footer.count('')

  wc = header_wc
  page = 1
  dst_file = file+'.'+str(page)+'.xml'
  dst = open(dst_file, 'w')
  dst.write(header)

  while True:
    s = read_item(src)
    wc += s.count('')
    dst.write(s)

    if (wc > limit or s == ''):
      dst.write(footer)
      wc += footer_wc
      dst.close()
      print dst_file + ': '+str(wc)+' chars'

      if (s == ''):
        break

      page+=1
      dst_file = file+'.'+str(page)+'.xml'
      dst = open(dst_file, 'w')
      dst.write(header)
      wc = header_wc


def read_header(f):
  s = ''
  while True:
    l = f.readline()
    if(l.find('<item>') > -1):
      break
    s += l
  return s


def read_item(f):
  s = ''
  while True:
    l = f.readline()
 
    # end of the file. 
    if (l=''):  
      return ''
    s += l
    if(l.find('</item>') > -1):
      break

  # This happens only in the 1st item.
  if (s.find('<item>') == -1):
    s = '<item>\n' + s
  return s 

#-------------------------------
if __name__ == "__main__":
    main()

