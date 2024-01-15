n,r,c = map(int,input().split())

def get_quadrant(i_start, i_end, j_start, j_end):             # r행 c열이 몇 사분면에 속하는지 구하기
    global r,c
    first_quad_end_i = (i_start + i_end) // 2
    first_quad_end_j = (j_start + j_end) // 2

    if i_start<=r<=first_quad_end_i and j_start<=c<=first_quad_end_j: 
        return (1, (i_start,first_quad_end_i,j_start,first_quad_end_j))
    elif i_start<=r<=first_quad_end_i and first_quad_end_j<c<=j_end: 
        return (2, (i_start,first_quad_end_i,first_quad_end_j+1,j_end))
    elif first_quad_end_i<r<=i_end and j_start<=c<=first_quad_end_j: 
        return (3, (first_quad_end_i+1,i_end,j_start,first_quad_end_j))
    elif first_quad_end_i<r<=i_end and first_quad_end_j<c<=j_end: 
        return (4, (first_quad_end_i+1,i_end,first_quad_end_j+1,j_end))

total_cnt = (2**n) * (2**n)
one_quad_cnt = total_cnt // 4
quad,quad_range = get_quadrant(0,2**n-1,0,2**n-1)
quad_start_num = 0 + one_quad_cnt*(quad-1)
      
while total_cnt >= 4:
    total_cnt = total_cnt // 4
    one_quad_cnt = total_cnt // 4
    quad, quad_range = get_quadrant(quad_range[0],quad_range[1],quad_range[2],quad_range[3])
    quad_start_num += one_quad_cnt * (quad-1)

print(quad_start_num)