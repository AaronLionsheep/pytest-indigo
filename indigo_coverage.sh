#!/bin/bash
ln -s src/pytest_indigo/indigo indigo

MODULES=$(python -m mypy.stubtest indigo --generate-allowlist)
ERRORS=$(python -m mypy.stubtest indigo --ignore-missing-stub --concise)

echo "# Indigo Implementation Coverage" > INDIGO_COVERAGE.md

for MODULE in $MODULES; do
    echo "## \`$MODULE\`" >> INDIGO_COVERAGE.md
    if echo "$ERRORS" | grep -Eq "$MODULE is not present at runtime"; then
        echo "Not implemented" >> INDIGO_COVERAGE.md
    else
        echo "$ERRORS" | grep -E "$MODULE " >> INDIGO_COVERAGE.md
    fi

    echo "" >> INDIGO_COVERAGE.md
done

python -m mypy.stubtest indigo --ignore-missing-stub

unlink indigo