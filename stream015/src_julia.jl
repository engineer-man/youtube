#!/usr/bin/env julia

function sphere_vol(r)
    return 4/3*pi*r^3
end

quadratic(a, sqr_term, b) = (-b + sqr_term) / 2a

function quadratic2(a::Float64, b::Float64, c::Float64)
    sqr_term = sqrt(b^2-4a*c)
    r1 = quadratic(a, sqr_term, b)
    r2 = quadratic(a, -sqr_term, b)
    r1, r2
end

vol = sphere_vol(3)
@printf "volume = %0.3f\n" vol

quad1, quad2 = quadratic2(2.0, -2.0, -12.0)
println("result 1: ", quad1)
println("result 2: ", quad2)
