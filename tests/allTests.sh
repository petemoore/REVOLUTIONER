ls | grep 'ests\.py$' | sort | while read TEST_MODULE
do
  echo "${TEST_MODULE}"
  python "${TEST_MODULE}" 2>&1 | grep -v '^$' |grep -v "^\-\-\-\-\-\-\-" | grep -v '^\.' | sed -e 's/.*/  &/'
done
