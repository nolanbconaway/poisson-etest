ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c Main program: computes the p-value of the unconditional test for testing
c one and two-sided hypotheses about the means of two Poisson
c distributions.
c
c INPUT:
c iside = side of the test; 1 for right-sided, 2 for two-sided
c alpha = nominal level of the test
c ki = count of the ith population, i = 1,2
c ni = sample size from the ith population, i=1,2
c d = the difference mean1 - mean2 under the H0
c
c OUTPUT:
c p-value = p-value of the unconditional test
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
	function two_sample_poisson(k1, k2, n1, n2, iside, d)
	implicit doubleprecision (a-h,o-z)
	elhatk = 1.0d0*(k1+k2)/(n1+n2)-d*n1/(n1+n2)
	var = (1.0d0*k1/n1**2 + 1.0d0*k2/n2**2)
	t_k1k2 = (1.0d0*k1/n1-1.0d0*k2/n2-d)/sqrt(var)
	call poistest(iside, n1, n2, elhatk, t_k1k2, d, pvalue)
	two_sample_poisson=pvalue
	return
	end

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c Program for computing the p-value of the unconditional test
c In the first subroutine, the sum over i1 is carried out
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

	subroutine poistest(iside, n1, n2, elhatk, t_k1k2, d, pvalue)
	implicit doubleprecision(a-h,o-z)
	intent(inout) :: pvalue

	pvalue = 0.0d0

c computing estimates of el1*n1 and el2*n2 under H_0
	elhat1 = n1*(elhatk+d)
	elhat2 = n2*elhatk

c computing the modes
	i1mode = int(elhat1)
	i2mode = int(elhat2)

c initializing the probability at the i1mode
	pi1mode = poipr(i1mode, elhat1)
	pi1 = pi1mode

c initializing the probability at the i2mode
	pi2mode = poipr(i2mode, elhat2)

	do i1 = i1mode, 1000
	  if(pi1 .lt. 1.0d-07) goto 1
	  call sumi2(iside, n1, n2, elhat2, t_k1k2, i1, pi1, i2mode,
     &             pi2mode, d, pvalue)
	  pi1 = elhat1*pi1/(i1+1.0d0)
	end do

1	i1 = i1mode-1
	pi1 = pi1mode
	pi1 = i1mode*pi1/elhat1

	do i1 = i1mode-1, 0, -1
	  if(pi1 .lt. 1.0d-07) return
	  call sumi2(iside, n1, n2, elhat2, t_k1k2, i1, pi1, i2mode,
     &             pi2mode, d, pvalue)
	  pi1 = i1*pi1/elhat1
	end do
	end

cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c Here, we carry out the sum over i2 to compute the p-value of the E-test
c
cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

	subroutine sumi2(iside, n1, n2, elhat2, t_k1k2, i1, pi1, i2mode,
     &                 pi2mode, d, pvalue)
	implicit doubleprecision(a-h,o-z)
	pi2 = pi2mode

	do i2 = i2mode, 1000
	  if(pi2 .lt. 1.0d-07) goto 1
	  elhati1 = 1.0d0*i1/n1
	  elhati2 = 1.0d0*i2/n2
	  diffi = elhati1 - elhati2 - d
	  var = (1.0d0*elhati1/n1 + 1.0d0*elhati2/n2)
	  if(iside .eq. 1) then
	    if(1.0d0*i1/n1 - 1.0d0*i2/n2 .le. d) then
	      t_i1i2 = 0.0d0
	    else
	      t_i1i2 = diffi/sqrt(var)
	    end if
	    if(t_i1i2 .ge. t_k1k2) pvalue = pvalue + pi1*pi2
	  else if(iside .eq. 2) then
	    if(dabs(1.0d0*i1/n1 - 1.0d0*i2/n2) .le. d) then
	      t_i1i2 = 0.0d0
	    else
	      t_i1i2 = diffi/sqrt(var)
	    end if
	    if(dabs(t_i1i2) .ge. dabs(t_k1k2)) pvalue = pvalue + pi1*pi2
	  end if
	  pi2 = elhat2*pi2/(i2+1.0d0)
	end do
c
1     i2 = i2mode-1
	pi2 = pi2mode
	pi2 = i2mode*pi2/elhat2

	do i2 = i2mode-1, 0, -1
	  if(pi2 .lt. 1.0d-07) return
	  elhati1 = 1.0d0*i1/n1
	  elhati2 = 1.0d0*i2/n2
	  diffi = elhati1 - elhati2 - d
	  var = (1.0d0*elhati1/n1 + 1.0d0*elhati2/n2)
	  if(iside .eq. 1) then
	    if(1.0d0*i1/n1 - 1.0d0*i2/n2 .le. d) then
	      t_i1i2 = 0.0d0
	    else
	      t_i1i2 = diffi/sqrt(var)
	    end if
	    if(t_i1i2 .ge. t_k1k2) pvalue = pvalue + pi1*pi2
	  else if(iside .eq. 2) then
	    if(dabs(1.0d0*i1/n1 - 1.0d0*i2/n2) .le. d) then
	      t_i1i2 = 0.0d0
	    else
	      t_i1i2 = diffi/sqrt(var)
	    end if
	    if(dabs(t_i1i2) .ge. dabs(t_k1k2)) pvalue = pvalue + pi1*pi2
	  end if
	  pi2 = i2*pi2/elhat2
	end do
	end

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c This program computes the P(X = k), where X is a Poisson random
c variable with mean defective rate = el, # of defective items = k
c
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

	double precision function poipr(k, el)
	implicit doubleprecision(a-h,o-z)

	ek = k*1.0d0
	poipr = dexp(-el+ek*dlog(el)-alng(ek+1.0d0))
	end

ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c Logarithmic gamma function = alng(x),  x > 0
c
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

        double precision function alng(x)
        implicit doubleprecision (a-h, o-z)
        double precision b(8)
        logical indx
        data b/8.33333333333333d-2, 3.33333333333333d-2,
     +         2.52380952380952d-1, 5.25606469002695d-1,
     +         1.01152306812684d0,  1.51747364915329d0,
     +         2.26948897420496d0,  3.00991738325940d0/
        if(x .lt. 8.0d0) then
        xx = x + 8.0d0
        indx = .true.
        else
        indx = .false.
        xx = x
        end if
c
        fterm = (xx-0.5d0)*dlog(xx) - xx + 9.1893853320467d-1
        sum = b(1)/(xx+b(2)/(xx+b(3)/(xx+b(4)/(xx+b(5)/(xx+b(6)
     +/(xx+b(7)/(xx+b(8))))))))
        alng = sum + fterm
        if(indx)  alng = alng-dlog(x+7.0d0)-dlog(x+6.0d0)-dlog
     +        (x+5.0d0)-dlog(x+4.0d0)-dlog(x+3.0d0)-dlog(x+2.0d0)
     +        -dlog(x+1.0d0)-dlog(x)
        end
