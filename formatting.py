print("{} {}, {}".format('ala', 'bala', 'portocala'))
print("{2} - {0} - {1}".format('ala', 'bala', 'portocala'))
print("{param2} - {param1}".format(param1='ala', param2='bala'))
print("{1} - {param} - {0}".format('ala', 'bala', param = 'portocala'))

print('%s %s' % ('ala', 'bala'))
print('%s - %i - %f' % ('ala', 34, 6.8))

print('ala {:>15} portocala'.format('bala'))
print('ala {:-<15} portocala'.format('bala'))

print('## {:_^14.4f} ##'.format(12.3))