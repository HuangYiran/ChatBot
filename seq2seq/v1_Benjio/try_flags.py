import tensorflow as tf

tf.app.flags.DEFINE_string('str_name', 'def_v_1', 'name of the user')
tf.app.flags.DEFINE_integer('age', 18, 'age of the user')
tf.app.flags.DEFINE_boolean('isSingle', True, 'is Single or not')

FLAGS = tf.app.flags.FLAGS

# must use parameter, otherwise: Typeerror:main() takes no arguments (1 given)';

def main(_):
    print(FLAGS.str_name)
    print(FLAGS.age)
    print(FLAGS.isSingle)

if __name__ == '__main__':
    tf.app.run()
