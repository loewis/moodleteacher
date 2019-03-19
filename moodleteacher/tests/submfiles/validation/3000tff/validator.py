from moodleteacher.tests import assert_raises, assert_dont_raises
from moodleteacher import compiler


def validate(job):
    assert_dont_raises(job.prepare_student_files)
    student_files = ['lib.c','lib.h','main.c']
    assert_dont_raises(job.run_build, compiler=compiler.GPP, inputs=student_files, output='add')
    assert_dont_raises(job.run_compiler, compiler=compiler.GPP, inputs=student_files, output='add')
    assert_dont_raises(job.run_make, mandatory=False)
    assert_raises(job.run_make, mandatory=True)
    assert_dont_raises(job.run_configure, mandatory=False)
    assert_raises(job.run_configure, mandatory=True)
