#!/usr/bin/env bash

# process go
rm run_go.go
go build src_go.go
mv src_go run_go.go

# process c
gcc -o run_c.c src_c.c

# process cpp
g++ -o run_cpp.cpp src_cpp.cpp

# process java
javac run_java.java

# process rust
rustc -o run_rust.rs src_rust.rs

in1=5
in2=5
output="50 3"

for language in run*; do
    res=
    case "$language" in
        run_java.java)
            continue
            ;;
        run_java.class)
            res=$(java run_java $in1 $in2)
            ;;
        run_cs.cs)
            res=$(sudo \
                docker run \
                    --rm \
                    -v $(pwd)/run_cs.cs:/src/run_cs.cs \
                    mono:latest \
                    bash -c "cd /src && mcs run_cs.cs -out:binary && mono binary $in1 $in2" \
                )
            ;;
        *)
            res=$(./$language $in1 $in2)
    esac

    if [[ $res == $output ]]; then
        echo "$language: $res (passed)"
    else
        echo "$language: $res (failed)"
    fi
done

rm run_c.c
rm run_cpp.cpp
rm run_java.class
rm run_rust.rs
