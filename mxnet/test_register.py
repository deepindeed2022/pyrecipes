#-*-encoding:utf-8-*-

class Optimizer(object):
	test_dict = {}

	@staticmethod
	def register(klass):
		name = klass.__name__.lower()
		print '{} is registing....'.format(name)
		if name in Optimizer.test_dict:
			print('WARNING: New test_item %s.%s is overriding '
				  'existing test_item %s.%s' % (
					  klass.__module__, klass.__name__,
					  Optimizer.test_dict[name].__module__,
					  Optimizer.test_dict[name].__name__))
		Optimizer.test_dict[name] = klass
		return klass

	@staticmethod
	def create_test_item(name, classes):
		if name.lower() in Optimizer.test_dict:
			return Optimizer.test_dict[name](classes)
		else:
			raise ValueError('Cannot find test_item %s' % name)

	def __init__(self, classes):
		self.classes = classes
		print 'Base class'

register = Optimizer.register

@register
class Cao(Optimizer):
	def __init__(self, classes):
		super(Cao, self).__init__(classes)
		print 'Cao Constructor'

	def output(self):
		print "Cao print"

if __name__ == '__main__':
	s = Optimizer.create_test_item('cao', 2)
	s.output()

# 小结
# 装饰器运行在代码运行之前，即定义阶段就已经完成