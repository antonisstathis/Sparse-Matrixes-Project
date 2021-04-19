from functions import create_weights,create_travels,add_node,calculate_product,print_data,calculate_min
import time

V=800
n=10000
a1_jloc=list()
a1_irow=list()
a1_jval=list()

# create travels
weights=create_weights(V)
create_travels(V,n,a1_jloc,a1_irow,a1_jval,weights)
print_data(a1_jloc,a1_irow,a1_jval)

# 1
add_node(V,n,a1_jloc,a1_irow,a1_jval,weights)

# 2
tic = time.perf_counter()
calculate_product(V,n,a1_irow,a1_jloc)
toc = time.perf_counter()
print(f"It took {toc - tic:0.4f} seconds to calculate the b=AT*A.\n\n\n")

# 3
tic = time.perf_counter()
calculate_min(V,n,a1_jloc,a1_irow,a1_jval)
toc = time.perf_counter()
print(f"It took {toc - tic:0.4f} seconds to find the destination with the fewest visits.\n\n\n")

# 4
V=800
n=20000
a1_jloc=list()
a1_irow=list()
a1_jval=list()
create_travels(V,n,a1_jloc,a1_irow,a1_jval,weights)

tic = time.perf_counter()
calculate_product(V,n,a1_irow,a1_jloc)
toc = time.perf_counter()
print(f"It took {toc - tic:0.4f} seconds to calculate the b=AT*A.\n\n\n")

tic = time.perf_counter()
calculate_min(V,n,a1_jloc,a1_irow,a1_jval)
toc = time.perf_counter()
print(f"It took {toc - tic:0.4f} seconds to find the destination with the fewest visits.\n\n\n")

print("The programm terminated successfully.")