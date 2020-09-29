from textwrap import dedent

from aiida_lammps.common.reaxff_convert import read_lammps_format, write_lammps_format

lammps_file1 = dedent(
    """\
        Reactive MD-force field: Cr/O/Fe/S/C/H force field 2014
        39 ! Number of general parameters
        50.0000 ! Overcoordination 1
        9.5469 ! Overcoordination 2
        26.5405 ! Valency angle conjugation 1
        1.7224 ! Triple bond stabilisation 1
        6.8702 ! Triple bond stabilisation 2
        60.4850 ! C2-correction
        1.0588 ! Undercoordination 1
        4.6000 ! Triple bond stabilisation
        12.1176 ! Undercoordination 2
        13.3056 ! Undercoordination 3
        -70.5044 ! Triple bond stabilization energy
        0.0000 ! Lower Taper-radius
        10.0000 ! Upper Taper-radius
        2.8793 ! Not used 1
        33.8667 ! Valency undercoordination
        6.0891 ! Valency angle/lone pair
        1.0563 ! Valency angle 1
        2.0384 ! Valency angle 2
        6.1431 ! Not used 2
        6.9290 ! Double bond/angle
        0.3989 ! Double bond/angle: overcoord 1
        3.9954 ! Double bond/angle: overcoord 2
        -2.4837 ! Not used 3
        5.7796 ! Torsion/BO
        10.0000 ! Torsion overcoordination 1
        1.9487 ! Torsion overcoordination 2
        -1.2327 ! Not used 4
        2.1645 ! Conjugation
        1.5591 ! vdWaals shielding
        0.1000 ! bond order cutoff
        2.1365 ! Valency angle conjugation 2
        0.6991 ! Valency overcoordination 1
        50.0000 ! Valency overcoordination 2
        1.8512 ! Valency/lone pair
        0.5000 ! Not used 5
        20.0000 ! Not used 6
        5.0000 ! Not used 7
        0.0000 ! Not used 8
        2.6962 ! Valency angle conjugation 3
        7 ! Nr of atoms; cov.r; valency;a.m;Rvdw;Evdw;gammaEEM;cov.r2;#
        alfa;gammavdW;valency;Eunder;Eover;chiEEM;etaEEM;n.u.
        cov r3;Elp;Heat inc.;n.u.;n.u.;n.u.;n.u.
        ov/un;val1;n.u.;val3,vval4
        C 1.3817 4.0000 12.0000 1.8903 0.1838 0.9000 1.1341 4.0000
        9.7559 2.1346 4.0000 34.9350 79.5548 5.9666 7.0000 0.0000
        1.2114 0.0000 202.5551 8.9539 34.9289 13.5366 0.8563 0.0000
        -2.8983 2.5000 1.0564 4.0000 2.9663 0.0000 0.0000 0.0000
        H 0.8930 1.0000 1.0080 1.3550 0.0930 0.8203 -0.1000 1.0000
        8.2230 33.2894 1.0000 0.0000 121.1250 3.7248 9.6093 1.0000
        -0.1000 0.0000 61.6606 3.0408 2.4197 0.0003 1.0698 0.0000
        -19.4571 4.2733 1.0338 1.0000 2.8793 0.0000 0.0000 0.0000
        O 1.2450 2.0000 15.9990 2.3890 0.1000 1.0898 1.0548 6.0000
        9.7300 13.8449 4.0000 37.5000 116.0768 8.5000 8.3122 2.0000
        0.9049 0.4056 59.0626 3.5027 0.7640 0.0021 0.9745 0.0000
        -3.5500 2.9000 1.0493 4.0000 2.9225 0.0000 0.0000 0.0000
        Fe 1.9029 3.0000 55.8450 2.0990 0.1181 0.4744 -1.6836 3.0000
        10.8548 2.6084 3.0000 0.0000 18.3725 1.7785 8.6281 0.0000
        -1.2000 0.0000 102.1000 25.3430 10.1260 0.7590 0.8563 0.0000
        -16.0573 2.6997 1.0338 6.0000 2.5791 0.0000 0.0000 0.0000
        S 1.8328 2.0000 32.0600 1.8815 0.3236 0.7530 1.6468 6.0000
        9.0000 4.9055 4.0000 30.0000 112.1416 6.5745 9.0000 2.0000
        1.0000 3.4994 65.0000 12.0000 22.1978 15.3230 0.9745 0.0000
        -15.7363 2.8802 1.0338 6.2998 2.8793 0.0000 0.0000 0.0000
        Cr 1.8921 6.0000 51.9962 2.3712 0.2336 0.5639 -1.6836 6.0000
        10.3177 2.8702 6.0000 0.0000 18.3190 1.4546 8.9500 0.0000
        -1.2000 0.0000 102.1000 25.3430 10.1260 0.7590 0.8563 0.0000
        -11.1953 2.6997 1.0338 6.0000 2.5791 0.0000 0.0000 0.0000
        X -0.1000 2.0000 1.0080 2.0000 0.0000 0.0100 -0.1000 6.0000
        10.0000 2.5000 4.0000 0.0000 0.0000 5.0001 9999.0000 0.0000
        -0.1000 0.0000 -2.3700 8.7410 13.3640 0.6690 0.9745 0.0000
        -11.0000 2.7466 1.0338 2.0000 2.8793 0.0000 0.0000 0.0000
        21 ! Nr of bonds; Edis1;LPpen;n.u.;pbe1;pbo5;13corr;pbo6
        pbe2;pbo3;pbo4;n.u.;pbo1;pbo2;ovcorr
        1 1 158.2004 99.1897 78.0000 -0.7738 -0.4550 1.0000 37.6117 0.4147
        0.4590 -0.1000 9.1628 1.0000 -0.0777 6.7268 1.0000 0.0000
        1 2 169.4760 0.0000 0.0000 -0.6083 0.0000 1.0000 6.0000 0.7652
        5.2290 1.0000 0.0000 1.0000 -0.0500 6.9136 0.0000 0.0000
        1 3 164.4303 82.6772 60.8077 -0.3739 -0.2351 1.0000 10.5036 1.0000
        0.4475 -0.2288 7.0250 1.0000 -0.1363 4.8734 0.0000 0.0000
        1 4 109.5214 0.0000 0.0000 0.6663 -0.3000 1.0000 36.0000 0.0100
        1.0648 -0.3500 15.0000 1.0000 -0.1512 4.1708 1.0000 0.0000
        1 5 192.1462 90.5383 55.2528 -0.5652 -0.5211 1.0000 18.9617 0.1958
        2.0000 -0.1016 13.8750 1.0000 -0.1579 5.5813 1.0000 0.0000
        1 6 0.0000 0.0000 0.0000 1.0000 -0.3000 1.0000 36.0000 0.5000
        0.3000 -0.3500 15.0000 1.0000 -0.2000 8.0000 1.0000 0.0000
        2 2 153.3934 0.0000 0.0000 -0.4600 0.0000 1.0000 6.0000 0.7300
        6.2500 1.0000 0.0000 1.0000 -0.0790 6.0552 0.0000 0.0000
        2 3 160.0000 0.0000 0.0000 -0.5725 0.0000 1.0000 6.0000 0.5626
        1.1150 1.0000 0.0000 0.0000 -0.0920 4.2790 0.0000 0.0000
        2 4 78.2669 0.0000 0.0000 0.4668 0.0000 1.0000 6.0000 0.1766
        0.5673 1.0000 0.0000 1.0000 -0.1543 5.4965 0.0000 0.0000
        2 5 188.3744 0.0000 0.0000 -0.6562 0.0000 1.0000 6.0000 0.3870
        11.8360 1.0000 0.0000 1.0000 -0.0762 5.0961 1.0000 0.0000
        2 6 0.0000 0.0000 0.0000 1.0000 -0.3000 1.0000 36.0000 0.5000
        0.3000 -0.3500 15.0000 1.0000 -0.2000 8.0000 1.0000 0.0000
        3 3 142.2858 145.0000 50.8293 0.2506 -0.1000 1.0000 29.7503 0.6051
        0.3451 -0.1055 9.0000 1.0000 -0.1225 5.5000 1.0000 0.0000
        3 4 67.5128 0.0000 0.0000 0.1301 -0.3000 0.0000 36.0000 0.0852
        1.0000 -0.3500 15.0000 1.0000 -0.0629 7.1208 0.0000 0.0000
        3 5 107.2917 202.9813 40.0000 0.4728 -0.2406 1.0000 22.1005 0.0500
        0.6528 -0.3341 7.9877 1.0000 -0.0909 6.9512 1.0000 0.0000
        3 6 114.0666 0.0000 0.0000 0.2305 -0.3000 1.0000 36.0000 0.6591
        0.5793 -0.3500 15.0000 1.0000 -0.1989 4.8803 1.0000 0.0000
        4 4 41.4611 0.0000 0.0000 0.2931 -0.2000 0.0000 16.0000 0.2682
        0.6294 -0.2000 15.0000 1.0000 -0.0512 6.8013 0.0000 0.0000
        4 5 75.5280 0.0000 0.0000 -0.4815 -0.3390 0.0000 16.0000 0.1769
        0.2800 -0.1838 15.0000 1.0000 -0.0758 6.3424 0.0000 0.0000
        4 6 41.4444 0.0000 0.0000 0.9374 -0.1000 0.0000 16.0000 0.0106
        0.2209 -0.2000 15.0000 1.0000 -0.0925 6.1220 0.0000 0.0000
        5 5 86.8868 69.1367 0.0000 -0.9993 -0.4781 1.0000 17.8574 0.0999
        0.2799 -0.1677 8.2557 1.0000 -0.1131 6.1440 1.0000 0.0000
        5 6 88.6258 0.0000 0.0000 0.6879 -0.3891 1.0000 36.0000 0.0835
        0.2900 -0.2339 12.1279 1.0000 -0.1166 5.6660 1.0000 0.0000
        6 6 57.5947 0.0000 0.0000 -1.0000 -0.3000 0.0000 16.0000 0.0100
        0.0842 -0.3000 16.0000 1.0000 -0.1098 5.3349 0.0000 0.0000
        15 ! Nr of off-diagonal terms; Ediss;Ro;gamma;rsigma;rpi;rpi2
        1 2 0.1239 1.4004 9.8467 1.1210 -1.0000 -1.0000
        1 3 0.1345 1.8422 9.7725 1.2835 1.1576 1.0637
        1 4 0.4204 1.4900 11.0144 1.4071 -1.0000 -1.0000
        1 5 0.3314 1.7976 10.5605 1.6918 1.4000 -1.0000
        1 6 0.1000 1.5000 11.0000 -1.0000 -1.0000 -1.0000
        2 3 0.0283 1.2885 10.9190 0.9215 -1.0000 -1.0000
        2 4 0.0200 1.9451 10.8595 1.4157 -1.0000 -1.0000
        2 5 0.1020 1.7528 9.6276 1.3714 -1.0000 -1.0000
        2 6 0.1000 1.5000 11.0000 -1.0000 -1.0000 -1.0000
        3 4 0.1000 1.8000 9.1989 1.7050 -1.0000 -1.0000
        3 5 0.2832 1.8196 10.2295 1.4502 1.4557 -1.0000
        3 6 0.0582 1.7000 11.6513 1.5924 -1.0000 -1.0000
        4 5 0.0854 1.7474 12.7924 1.9838 -1.0000 -1.0000
        4 6 0.3236 2.1670 10.1297 1.9025 -1.0000 -1.0000
        5 6 0.2523 1.9844 10.1396 1.8938 -1.0000 -1.0000
        115 ! Nr of angles;at1;at2;at3;Thetao,o;ka;kb;pv1;pv2
        1 1 1 59.0573 30.7029 0.7606 0.0000 0.7180 6.2933 1.1244
        1 1 2 65.7758 14.5234 6.2481 0.0000 0.5665 0.0000 1.6255
        1 1 3 53.9517 7.8968 2.6122 0.0000 3.0000 58.6562 1.0338
        1 1 4 74.8790 30.0000 2.0000 0.0000 2.0334 0.0000 1.0928
        1 1 5 71.4462 27.2223 6.7228 0.0000 0.0050 0.0000 2.6454
        1 1 6 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        1 2 1 0.0000 3.4110 7.7350 0.0000 0.0000 0.0000 1.0400
        1 2 2 0.0000 0.0000 6.0000 0.0000 0.0000 0.0000 1.0400
        1 2 3 0.0000 25.0000 3.0000 0.0000 1.0000 0.0000 1.0400
        1 2 4 0.0000 0.0100 2.2066 0.0000 1.9789 0.0000 1.4466
        1 2 5 0.0000 0.2500 6.0000 0.0000 0.0000 0.0000 1.0400
        1 2 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        1 3 1 72.6199 42.5510 0.7205 0.0000 2.9294 0.0000 1.3096
        1 3 2 70.1101 13.1217 4.4734 0.0000 0.8433 0.0000 3.0000
        1 3 3 81.9029 32.2258 1.7397 0.0000 0.9888 68.1072 1.7777
        1 3 4 90.0000 42.4716 6.6776 0.0000 2.4560 0.0000 1.6221
        1 3 5 83.1032 23.4174 0.7741 0.0000 1.2168 0.0000 2.7365
        1 3 6 63.7706 34.5234 0.9493 0.0000 2.4647 0.0000 1.7747
        1 4 1 0.1000 42.2980 0.3169 0.0000 1.1069 0.0000 2.3466
        1 4 2 42.7140 0.1451 0.2500 0.0000 0.0851 0.0000 2.8955
        1 4 3 38.2755 19.3103 0.1151 0.0000 0.7569 0.0000 2.3113
        1 4 4 47.9341 1.0246 7.9341 0.0000 2.8853 0.0000 1.0000
        1 4 5 60.3275 30.0000 1.0871 0.0000 1.3106 0.0000 1.6977
        1 4 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        1 5 1 92.6710 15.6798 3.1104 0.0000 0.3458 0.0000 2.3207
        1 5 2 99.1897 14.1666 2.5588 0.0000 0.3542 0.0000 2.5990
        1 5 3 79.9791 29.5117 7.0000 0.0000 0.0050 0.0000 1.2255
        1 5 4 67.5806 21.4421 0.9049 0.0000 0.7789 0.0000 1.2000
        1 5 5 89.3910 5.0000 7.0000 0.0000 1.0050 0.0000 1.5000
        1 5 6 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        1 6 1 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        1 6 2 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        1 6 3 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        1 6 4 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        1 6 5 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        1 6 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        2 1 2 70.2607 25.2202 3.7312 0.0000 0.0050 0.0000 2.7500
        2 1 3 65.0000 16.3141 5.2730 0.0000 0.4448 0.0000 1.4077
        2 1 4 2.6539 32.1638 0.9167 0.0000 0.0240 0.0000 1.1158
        2 1 5 43.6595 11.8933 0.5449 0.0000 0.0050 0.0000 1.9326
        2 1 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        2 2 2 0.0000 27.9213 5.8635 0.0000 0.0000 0.0000 1.0400
        2 2 3 0.0000 8.5744 3.0000 0.0000 0.0000 0.0000 1.0421
        2 2 4 0.0000 0.0100 1.0568 0.0000 1.8595 0.0000 3.6142
        2 2 6 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        2 3 2 85.8000 9.8453 2.2720 0.0000 2.8635 0.0000 1.5800
        2 3 3 75.6935 50.0000 2.0000 0.0000 1.0000 0.0000 1.1680
        2 3 4 26.0012 49.6772 0.0500 0.0000 1.1589 0.0000 1.0000
        2 3 5 35.9099 19.1501 1.9918 0.0000 0.9342 0.0000 2.7883
        2 3 6 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        2 4 2 20.3683 0.0100 2.2825 0.0000 0.7660 0.0000 1.3788
        2 4 3 38.5594 11.2599 0.1898 0.0000 0.1904 0.0000 1.4041
        2 4 4 48.4128 4.0632 0.6773 0.0000 2.2274 0.0000 1.8605
        2 4 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        2 5 2 90.0601 42.2756 0.5302 0.0000 0.3707 0.0000 1.0071
        2 5 4 84.8837 16.4865 0.8240 0.5000 0.5428 0.0000 1.1398
        2 5 5 66.1035 8.0885 1.0424 0.0000 0.7355 0.0000 3.0000
        2 5 6 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        2 6 2 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        2 6 3 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        2 6 4 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        2 6 5 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        2 6 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        3 1 3 76.9627 44.2852 2.4177 -25.3063 1.6334 -50.0000 2.7392
        3 1 4 54.6900 12.6123 2.3543 0.0000 2.0000 0.0000 1.2513
        3 1 6 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0500
        3 2 3 0.0000 15.0000 2.8900 0.0000 0.0000 0.0000 2.8774
        3 2 4 0.0000 0.0100 3.2567 0.0000 2.0582 0.0000 1.3513
        3 2 5 0.0000 1.0000 6.0000 0.0000 0.0000 0.0000 1.0400
        3 2 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        3 3 3 80.7324 30.4554 0.9953 0.0000 3.0000 50.0000 1.0783
        3 3 4 73.6721 32.6330 1.7223 0.0000 1.0221 0.0000 1.4351
        3 3 5 60.2631 30.0701 2.1707 0.0000 1.3323 0.0000 1.0192
        3 3 6 44.9499 30.0000 4.2281 0.0000 1.6672 0.0000 1.2000
        3 4 3 76.5431 0.0583 0.0500 0.0000 0.4968 0.0000 2.2792
        3 4 4 69.4895 5.7742 8.0001 0.0000 1.7794 0.0000 2.7889
        3 4 5 29.3282 8.1452 2.8121 0.0000 0.2287 0.0000 1.9412
        3 4 6 41.9243 20.0000 2.9881 0.0000 1.2678 0.0000 2.6481
        3 5 3 83.5231 37.5859 0.9881 -0.0100 1.4725 0.0000 1.0641
        3 5 4 89.9073 7.0973 1.3919 0.0000 0.8210 0.0000 2.9921
        3 5 5 55.9402 38.2990 3.6930 0.0000 2.2673 0.0000 1.0000
        3 5 6 83.6415 19.7500 2.9247 0.0000 1.9437 0.0000 1.0348
        3 6 3 63.9878 12.9742 3.0000 0.0000 0.5058 0.0000 3.0000
        3 6 4 44.3862 26.6099 2.0221 0.0000 1.9212 0.0000 3.0000
        3 6 5 19.4072 10.4590 2.8285 0.0000 1.0074 0.0000 2.3949
        3 6 6 51.2416 17.2148 0.3698 0.0000 1.5585 0.0000 1.5755
        4 1 4 33.2812 34.6443 3.0111 0.0000 0.1701 0.0000 1.0510
        4 1 5 89.6657 30.0000 3.0000 0.0000 2.0000 0.0000 1.2000
        4 1 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        4 2 4 0.0000 10.4428 7.9607 0.0000 2.3717 0.0000 1.1970
        4 2 5 0.0000 10.0000 1.0000 0.5000 0.2500 0.0000 1.5000
        4 2 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        4 3 4 63.0740 14.8127 2.9929 0.0000 0.7552 0.0000 1.3634
        4 3 5 4.8461 5.5458 2.9681 0.0000 1.0491 0.0000 1.4836
        4 3 6 61.0461 0.2600 1.3988 0.0000 0.9535 0.0000 3.0000
        4 4 5 33.4003 16.6274 0.1076 0.0000 0.0825 0.0000 1.0000
        4 5 4 100.0000 9.2519 0.7752 0.0000 0.1221 0.0000 2.2142
        4 5 5 77.0475 7.4569 4.9579 0.0000 0.7548 0.0000 2.3345
        4 5 6 93.8709 16.3822 1.8851 0.0000 0.3210 0.0000 1.9357
        4 6 5 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0000
        5 1 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        5 2 5 0.0000 7.5000 2.0000 0.0000 0.0000 0.0000 1.0400
        5 2 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        5 3 5 76.3546 40.0000 3.3161 0.0005 1.9473 0.0000 1.0000
        5 3 6 89.6617 15.3276 2.7567 0.0000 1.6031 0.0000 1.0781
        5 4 5 0.2000 7.5083 1.3736 0.0000 0.0412 0.0000 1.8149
        5 4 6 0.2000 7.5083 1.3736 0.0000 0.0412 0.0000 1.8149
        5 5 5 84.2345 15.5790 3.7715 0.0000 1.3066 0.0000 1.6270
        5 5 6 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0000
        5 6 5 70.0000 20.0000 2.0000 0.0000 1.0000 0.0000 1.0000
        5 6 6 50.5809 19.2597 0.3584 0.0000 0.2153 0.0000 1.6345
        6 1 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        6 2 6 0.0000 0.0000 1.0000 0.0000 1.0000 0.0000 1.0500
        6 3 6 54.9212 26.4957 1.1780 0.0000 2.0000 0.0000 2.2398
        6 5 6 87.7418 23.5125 2.9950 0.0000 0.5199 0.0000 1.6571
        37 ! Nr of torsions;at1;at2;at3;at4;;V1;V2;V3;V2(BO);vconj;n.u;n
        0 1 1 0 0.0000 50.0000 0.3000 -4.0000 0.0000 0.0000 0.0000
        0 1 2 0 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
        0 1 5 0 0.5000 50.0000 0.5000 -10.0000 0.0000 0.0000 0.0000
        0 2 2 0 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
        0 2 3 0 0.0000 0.1000 0.0200 -2.5415 0.0000 0.0000 0.0000
        0 2 5 0 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
        0 3 3 0 0.5511 25.4150 1.1330 -5.1903 -1.0000 0.0000 0.0000
        0 3 5 0 0.5000 50.0000 0.5000 -8.0000 0.0000 0.0000 0.0000
        1 1 1 1 -0.2500 34.7453 0.0288 -6.3507 -1.6000 0.0000 0.0000
        1 1 1 2 -0.2500 29.2131 0.2945 -4.9581 -2.1802 0.0000 0.0000
        1 1 1 3 1.2799 20.7787 -0.5249 -2.5000 -1.0000 0.0000 0.0000
        1 1 3 1 0.4816 19.6316 -0.0057 -2.5000 -1.0000 0.0000 0.0000
        1 1 3 2 1.2044 80.0000 -0.3139 -6.1481 -1.0000 0.0000 0.0000
        1 1 3 3 -0.0002 20.1851 0.1601 -9.0000 -2.0000 0.0000 0.0000
        1 3 3 1 0.0002 80.0000 -1.5000 -4.4848 -2.0000 0.0000 0.0000
        1 3 3 2 -2.5000 0.1181 0.0268 -5.4085 -2.9498 0.0000 0.0000
        1 3 3 3 0.4118 0.5219 0.9706 -2.5004 -0.9972 0.0000 0.0000
        1 5 5 1 0.0000 50.0000 0.0000 -8.0000 0.0000 0.0000 0.0000
        1 5 5 2 0.0000 50.0000 0.0000 -8.0000 0.0000 0.0000 0.0000
        2 1 1 2 -0.2500 31.2081 0.4539 -4.8923 -2.2677 0.0000 0.0000
        2 1 1 3 1.9159 19.8113 0.7914 -4.6995 -1.0000 0.0000 0.0000
        2 1 3 1 -2.5000 31.0191 0.6165 -2.7733 -2.9807 0.0000 0.0000
        2 1 3 2 -2.4875 70.8145 0.7582 -4.2274 -3.0000 0.0000 0.0000
        2 1 3 3 -1.4383 80.0000 1.0000 -3.6877 -2.8000 0.0000 0.0000
        2 1 4 4 0.0000 0.0000 0.0000 -5.0000 0.0000 0.0000 0.0000
        2 3 3 2 0.1995 5.0000 0.2000 -2.6000 0.0000 0.0000 0.0000
        2 3 3 3 0.1000 43.1840 0.5000 -6.6539 0.0000 0.0000 0.0000
        2 3 5 3 2.5000 2.5000 0.2237 -10.0000 0.0000 0.0000 0.0000
        2 5 5 2 0.0000 50.0000 0.0000 -8.0000 0.0000 0.0000 0.0000
        3 1 1 3 -1.4477 16.6853 0.6461 -4.9622 -1.0000 0.0000 0.0000
        3 1 3 1 -1.1390 78.0747 -0.0964 -4.5172 -3.0000 0.0000 0.0000
        3 1 3 2 -2.5000 70.3345 -1.0000 -5.5315 -3.0000 0.0000 0.0000
        3 1 3 3 -0.1583 20.0000 1.5000 -9.0000 -2.0000 0.0000 0.0000
        3 3 3 3 0.1000 1.0000 0.1000 -2.5000 -0.9000 0.0000 0.0000
        3 5 5 3 0.2500 90.0000 0.5000 -6.0000 0.0000 0.0000 0.0000
        3 5 5 5 0.2500 90.0000 0.5000 -6.0000 0.0000 0.0000 0.0000
        5 5 5 5 2.4661 71.9719 0.0100 -8.0000 0.0000 0.0000 0.0000
        4 ! Nr of hydrogen bonds;at1;at2;at3;Rhb;Dehb;vhb1
        3 2 3 2.1200 -3.5800 1.4500 19.5000
        3 2 5 2.5000 -1.0000 1.4500 19.5000
        5 2 3 2.5000 -1.0000 1.4500 19.5000
        5 2 5 2.5000 -2.0000 1.4500 19.5000
        """
)

lammps_file2 = dedent(
    """\
    Reactive MD-force field c/h/o combustion force field
    39       ! Number of general parameters
    50.0000 !p(boc1)
        9.5469 !p(boc2)
    26.5405 !p(coa2)
        1.5105 !p(trip4)
        6.6630 !p(trip3)
    70.0000 !kc2
        1.0588 !p(ovun6)
        4.6000 !p(trip2)
    12.1176 !p(ovun7)
    13.3056 !p(ovun8)
    -70.1292 !p(trip1)
        0.0000 !Lower Taper-radius (swa)
    10.0000 !Upper Taper-radius (swb)
        0.0000 !not used
    33.8667 !p(val7)
        6.0891 !p(lp1)
        1.0563 !p(val9)
        2.0384 !p(val10)
        6.1431 !not used
        6.9290 !p(pen2)
        0.3989 !p(pen3)
        3.9954 !p(pen4)
        0.0000 !not used
        5.7796 !p(tor2)
    10.0000 !p(tor3)
        1.9487 !p(tor4)
        0.0000 !not used
        2.1645 !p(cot2)
        1.5591 !p(vdW1)
        0.1000 !Cutoff for bond order*100 (cutoff)
        2.1365 !p(coa4)
        0.6991 !p(ovun4)
    50.0000 !p(ovun3)
        1.8512 !p(val8)
        0.0000 !not used
        0.0000 !not used
        0.0000 !not used
        0.0000 !not used
        2.6962 !p(coa3)
    3    ! Nr of atoms; atomID;ro(sigma); Val;atom mass;Rvdw;Dij;gamma;ro(pi);Val(e)
                alfa;gamma(w);Val(angle);p(ovun5);n.u.;chiEEM;etaEEM;n.u.
                ro(pipi);p(lp2);Heat increment;p(boc4);p(boc3);p(boc5),n.u.;n.u.
                p(ovun2);p(val3);n.u.;Val(boc);p(val5);n.u.;n.u.;n.u.
    C    1.3825   4.0000  12.0000   1.9133   0.1853   0.9000   1.1359   4.0000
        9.7602   2.1346   4.0000  33.2433  79.5548   5.8678   7.0000   0.0000
        1.2104   0.0000 199.0303   8.6991  34.7289  13.3894   0.8563   0.0000
        -2.8983   2.5000   1.0564   4.0000   2.9663   0.0000   0.0000   0.0000
    H    0.7853   1.0000   1.0080   1.5904   0.0419   1.0206  -0.1000   1.0000
        9.3557   5.0518   1.0000   0.0000 121.1250   5.3200   7.4366   1.0000
        -0.1000   0.0000  62.4879   1.9771   3.3517   0.7571   1.0698   0.0000
        -15.7683   2.1488   1.0338   1.0000   2.8793   0.0000   0.0000   0.0000
    O    1.2477   2.0000  15.9990   1.9236   0.0904   1.0503   1.0863   6.0000
        10.2127   7.7719   4.0000  36.9573 116.0768   8.5000   8.9989   2.0000
        0.9088   1.0003  60.8726  20.4140   3.3754   0.2702   0.9745   0.0000
        -3.6141   2.7025   1.0493   4.0000   2.9225   0.0000   0.0000   0.0000
    6      ! Nr of bonds; at1;at2;De(sigma);De(pi);De(pipi);p(be1);p(bo5);13corr;n.u.;p(bo6),p(ovun1)
                        p(be2);p(bo3);p(bo4);n.u.;p(bo1);p(bo2)
    1  1 156.5953 100.0397  80.0000  -0.8157  -0.4591   1.0000  37.7369   0.4235
            0.4527  -0.1000   9.2605   1.0000  -0.0750   6.8316   1.0000   0.0000
    1  2 170.2316   0.0000   0.0000  -0.5931   0.0000   1.0000   6.0000   0.7140
            5.2267   1.0000   0.0000   1.0000  -0.0500   6.8315   0.0000   0.0000
    2  2 156.0973   0.0000   0.0000  -0.1377   0.0000   1.0000   6.0000   0.8240
            2.9907   1.0000   0.0000   1.0000  -0.0593   4.8358   0.0000   0.0000
    1  3 160.4802 105.1693  23.3059  -0.3873  -0.1613   1.0000  10.8851   1.0000
            0.5341  -0.3174   7.0303   1.0000  -0.1463   5.2913   0.0000   0.0000
    3  3  60.1463 176.6202  51.1430  -0.2802  -0.1244   1.0000  29.6439   0.9114
            0.2441  -0.1239   7.6487   1.0000  -0.1302   6.2919   1.0000   0.0000
    2  3 180.4373   0.0000   0.0000  -0.8074   0.0000   1.0000   6.0000   0.5514
            1.2490   1.0000   0.0000   1.0000  -0.0657   5.0451   0.0000   0.0000
    3    ! Nr of off-diagonal terms. at1;at2;Dij;RvdW;alfa;ro(sigma);ro(pi);ro(pipi)
    1  2   0.1219   1.4000   9.8442   1.1203  -1.0000  -1.0000
    2  3   0.0344   1.6800  10.3247   0.9013  -1.0000  -1.0000
    1  3   0.1131   1.8523   9.8442   1.2775   1.1342   1.0621
    18    ! Nr of angles. at1;at2;at3;Thetao,o;p(val1);p(val2);p(coa1);p(val7);p(pen1);p(val4)
    1  1  1  67.2326  22.0695   1.6286   0.0000   1.7959  15.4141   1.8089
    1  1  2  65.2527  14.3185   6.2977   0.0000   0.5645   0.0000   1.1530
    2  1  2  70.0840  25.3540   3.4508   0.0000   0.0050   0.0000   3.0000
    1  2  2   0.0000   0.0000   6.0000   0.0000   0.0000   0.0000   1.0400
    1  2  1   0.0000   3.4110   7.7350   0.0000   0.0000   0.0000   1.0400
    2  2  2   0.0000  27.9213   5.8635   0.0000   0.0000   0.0000   1.0400
    1  1  3  49.5561   7.3771   4.9568   0.0000   0.7533  15.9906   1.0010
    3  1  3  77.1171  39.8746   2.5403 -24.3902   1.7740 -42.9758   2.1240
    2  1  3  65.0000  14.2057   4.8649   0.0000   0.3504   0.0000   1.7185
    1  3  1  74.3994  44.7500   0.7982   0.0000   3.0000   0.0000   1.0528
    1  3  3  77.9854  36.6201   2.0201   0.0000   0.7434  67.0264   3.0000
    3  3  3  80.7324  30.4554   0.9953   0.0000   1.6310  50.0000   1.0783
    1  3  2  71.5018  21.7062   0.4735   0.0000   0.5186   0.0000   1.1793
    2  3  3  84.9468  23.3540   1.5057   0.0000   2.6374   0.0000   1.3023
    2  3  2  77.0645  10.4737   1.2895   0.0000   0.9924   0.0000   1.1043
    1  2  3   0.0000  25.0000   3.0000   0.0000   1.0000   0.0000   1.0400
    3  2  3   0.0000   0.0148   6.0000   0.0000   0.0000   0.0000   1.0400
    2  2  3   0.0000   9.7025   6.0000   0.0000   0.0000   0.0000   1.0400
    26    ! Nr of torsions. at1;at2;at3;at4;;V1;V2;V3;p(tor1);p(cot1);n.u;n.u.
    1  1  1  1  -0.2500  11.5822   0.1879  -4.7057  -2.2047   0.0000   0.0000
    1  1  1  2  -0.2500  31.2596   0.1709  -4.6391  -1.9002   0.0000   0.0000
    2  1  1  2  -0.1770  30.0252   0.4340  -5.0019  -2.0697   0.0000   0.0000
    1  1  1  3  -0.7098  22.2951   0.0060  -2.5000  -2.1688   0.0000   0.0000
    2  1  1  3  -0.3568  22.6472   0.6045  -4.0088  -1.0000   0.0000   0.0000
    3  1  1  3  -0.0528   6.8150   0.7498  -5.0913  -1.0000   0.0000   0.0000
    1  1  3  1   2.0007  25.5641  -0.0608  -2.6456  -1.1766   0.0000   0.0000
    1  1  3  2  -1.1953  42.1545  -1.0000  -8.0821  -1.0000   0.0000   0.0000
    2  1  3  1  -0.9284  34.3952   0.7285  -2.5440  -2.4641   0.0000   0.0000
    2  1  3  2  -2.5000  79.6980   1.0000  -3.5697  -2.7501   0.0000   0.0000
    1  1  3  3  -0.0179   5.0603  -0.1894  -2.5000  -2.0399   0.0000   0.0000
    2  1  3  3  -0.5583  80.0000   1.0000  -4.4000  -3.0000   0.0000   0.0000
    3  1  3  1  -2.5000  76.0427  -0.0141  -3.7586  -2.9000   0.0000   0.0000
    3  1  3  2   0.0345  78.9586  -0.6810  -4.1777  -3.0000   0.0000   0.0000
    3  1  3  3  -2.5000  66.3525   0.3986  -3.0293  -3.0000   0.0000   0.0000
    1  3  3  1   2.5000  -0.5332   1.0000  -3.5096  -2.9000   0.0000   0.0000
    1  3  3  2  -2.5000   3.3219   0.7180  -5.2021  -2.9330   0.0000   0.0000
    2  3  3  2   2.2500  -6.2288   1.0000  -2.6189  -1.0000   0.0000   0.0000
    1  3  3  3   0.0531 -17.3983   1.0000  -2.5000  -2.1584   0.0000   0.0000
    2  3  3  3   0.4723 -12.4144  -1.0000  -2.5000  -1.0000   0.0000   0.0000
    3  3  3  3  -2.5000 -25.0000   1.0000  -2.5000  -1.0000   0.0000   0.0000
    0  1  2  0   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
    0  2  2  0   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000
    0  2  3  0   0.0000   0.1000   0.0200  -2.5415   0.0000   0.0000   0.0000
    0  1  1  0   0.0000  50.0000   0.3000  -4.0000  -2.0000   0.0000   0.0000
    0  3  3  0   0.5511  25.4150   1.1330  -5.1903  -1.0000   0.0000   0.0000
    1    ! Nr of hydrogen bonds. at1;at2;at3;r(hb);p(hb1);p(hb2);p(hb3)
    3  2  3   1.9682  -4.4628   1.7976   3.0000
    """
)


def test_read_lammps_format(data_regression):
    output = read_lammps_format(lammps_file1.splitlines())
    data_regression.check(output)


def test_round_trip_lammps_format(file_regression):
    data = read_lammps_format(lammps_file1.splitlines())
    output = write_lammps_format(data)
    file_regression.check(output)


def test_read_lammps_format2(data_regression):
    output = read_lammps_format(lammps_file2.splitlines())
    data_regression.check(output)


def test_round_trip_lammps_format2(file_regression):
    data = read_lammps_format(lammps_file2.splitlines())
    output = write_lammps_format(data)
    file_regression.check(output)
