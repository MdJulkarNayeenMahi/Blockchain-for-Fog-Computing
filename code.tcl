
set ns [new Simulator]

$ns color 0 green

set f0 [open Cloud.tr w]
set f1 [open Fog1.tr w]
set f2 [open Edge2.tr w]
set f3 [open Edge3.tr w]
set f4 [open Edge4.tr w]
set f5 [open Edge5.tr w]
set f6 [open Edge6.tr w]
set f7 [open Edge7.tr w]
set f8 [open Edge8.tr w]
set f9 [open Edge9.tr w]
set f10 [open Edge10.tr w]
set f11 [open Edge11.tr w]
set f12 [open Edge12.tr w]
set f13 [open Edge13.tr w]
set f14 [open Edge14.tr w]
set f15 [open Edge15.tr w]
set f16 [open Edge16.tr w]
set f17 [open Edge17.tr w]
set f18 [open Fog2.tr w]
set f19 [open Edge19.tr w]
set f20 [open Edge20.tr w]
set f21 [open Edge21.tr w]
set f22 [open Edge22.tr w]
set f23 [open Edge23.tr w]
set f24 [open Edge24.tr w]
set f25 [open Edge25.tr w]
set f26 [open Edge26.tr w]
set f27 [open Edge27.tr w]
set f28 [open Edge28.tr w]
set f29 [open Edge29.tr w]
set f30 [open Edge30.tr w]
set f31 [open Edge31.tr w]
set f32 [open Edge32.tr w]
set f33 [open Edge33.tr w]
set f34 [open output34.nam w]
$ns namtrace-all $f34

#node
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]
set n8 [$ns node]
set n9 [$ns node]
set n10 [$ns node]
set n11 [$ns node]
set n12 [$ns node]
set n13 [$ns node]
set n14 [$ns node]
set n15 [$ns node]
set n16 [$ns node]
set n17 [$ns node]
set n18 [$ns node]
set n19 [$ns node]
set n20 [$ns node]
set n21 [$ns node]
set n22 [$ns node]
set n23 [$ns node]
set n24 [$ns node]
set n25 [$ns node]
set n26 [$ns node]
set n27 [$ns node]
set n28 [$ns node]
set n29 [$ns node]
set n30 [$ns node]
set n31 [$ns node]
set n32 [$ns node]
set n33 [$ns node]
set n34 [$ns node]


#node link
$ns duplex-link $n0 $n1 1Mb 65ms DropTail
$ns duplex-link $n1 $n2 1Mb 65ms DropTail
$ns duplex-link $n2 $n3 1Mb 30ms DropTail
$ns duplex-link $n3 $n4 1Mb 30ms DropTail
$ns duplex-link $n4 $n5 1Mb 30ms DropTail
$ns duplex-link $n5 $n2 1Mb 30ms DropTail
#inside
$ns duplex-link $n2 $n4 1Mb 50ms DropTail
$ns duplex-link $n5 $n3 1Mb 50ms DropTail
#2nd block
$ns duplex-link $n4 $n6 1Mb 20ms DropTail
$ns duplex-link $n6 $n7 1Mb 30ms DropTail
$ns duplex-link $n7 $n8 1Mb 30ms DropTail
$ns duplex-link $n8 $n9 1Mb 30ms DropTail
$ns duplex-link $n9 $n6 1Mb 30ms DropTail
#inside
$ns duplex-link $n6 $n8 1Mb 50ms DropTail
$ns duplex-link $n9 $n7 1Mb 50ms DropTail
#3rd block
$ns duplex-link $n3 $n10 1Mb 30ms DropTail
$ns duplex-link $n10 $n11 1Mb 30ms DropTail
$ns duplex-link $n11 $n12 1Mb 30ms DropTail
$ns duplex-link $n12 $n13 1Mb 30ms DropTail
$ns duplex-link $n13 $n10 1Mb 30ms DropTail
#inside
$ns duplex-link $n10 $n12 1Mb 50ms DropTail
$ns duplex-link $n13 $n11 1Mb 50ms DropTail
#4th block
$ns duplex-link $n5 $n14 1Mb 30ms DropTail
$ns duplex-link $n14 $n15 1Mb 30ms DropTail
$ns duplex-link $n15 $n16 1Mb 30ms DropTail
$ns duplex-link $n16 $n17 1Mb 30ms DropTail
$ns duplex-link $n17 $n14 1Mb 30ms DropTail
#inside
$ns duplex-link $n14 $n16 1Mb 50ms DropTail
$ns duplex-link $n17 $n15 1Mb 50ms DropTail

#right side
$ns duplex-link $n0 $n18 1Mb 65ms DropTail
$ns duplex-link $n18 $n19 1Mb 65ms DropTail
$ns duplex-link $n19 $n20 1Mb 30ms DropTail
$ns duplex-link $n20 $n21 1Mb 30ms DropTail
$ns duplex-link $n21 $n22 1Mb 30ms DropTail
$ns duplex-link $n22 $n19 1Mb 30ms DropTail
#inside
$ns duplex-link $n19 $n21 1Mb 50ms DropTail
$ns duplex-link $n22 $n20 1Mb 50ms DropTail
#2nd block
$ns duplex-link $n21 $n23 1Mb 20ms DropTail
$ns duplex-link $n23 $n24 1Mb 30ms DropTail
$ns duplex-link $n24 $n25 1Mb 30ms DropTail
$ns duplex-link $n25 $n26 1Mb 30ms DropTail
$ns duplex-link $n26 $n23 1Mb 30ms DropTail
#inside
$ns duplex-link $n23 $n25 1Mb 50ms DropTail
$ns duplex-link $n26 $n24 1Mb 50ms DropTail
#3rd block
$ns duplex-link $n20 $n27 1Mb 30ms DropTail
$ns duplex-link $n27 $n28 1Mb 30ms DropTail
$ns duplex-link $n28 $n29 1Mb 30ms DropTail
$ns duplex-link $n29 $n30 1Mb 30ms DropTail
$ns duplex-link $n30 $n27 1Mb 30ms DropTail
#inside
$ns duplex-link $n27 $n29 1Mb 50ms DropTail
$ns duplex-link $n30 $n28 1Mb 50ms DropTail
#4th block
$ns duplex-link $n22 $n31 1Mb 30ms DropTail
$ns duplex-link $n31 $n32 1Mb 30ms DropTail
$ns duplex-link $n32 $n33 1Mb 30ms DropTail
$ns duplex-link $n33 $n34 1Mb 30ms DropTail
$ns duplex-link $n34 $n31 1Mb 30ms DropTail
#inside
$ns duplex-link $n31 $n33 1Mb 50ms DropTail
$ns duplex-link $n34 $n32 1Mb 50ms DropTail




#node position
$ns duplex-link-op $n0 $n1 orient left-down
$ns duplex-link-op $n1 $n2 orient left-down
$ns duplex-link-op $n2 $n3 orient right-down
$ns duplex-link-op $n3 $n4 orient left-down
$ns duplex-link-op $n4 $n5 orient left-up
$ns duplex-link-op $n5 $n2 orient right-up
#inside
$ns duplex-link-op $n2 $n4 orient down
$ns duplex-link-op $n5 $n3 orient right
#2nd block
$ns duplex-link-op $n4 $n6 orient down
$ns duplex-link-op $n6 $n7 orient right-down
$ns duplex-link-op $n7 $n8 orient left-down
$ns duplex-link-op $n8 $n9 orient left-up
$ns duplex-link-op $n9 $n6 orient right-up
#inside
$ns duplex-link-op $n6 $n8 orient down
$ns duplex-link-op $n9 $n7 orient right
#3rd block
$ns duplex-link-op $n3 $n10 orient right-down
$ns duplex-link-op $n10 $n11 orient right-down
$ns duplex-link-op $n11 $n12 orient left-down
$ns duplex-link-op $n12 $n13 orient left-up
$ns duplex-link-op $n13 $n10 orient right-up
#inside
$ns duplex-link-op $n10 $n12 orient down
$ns duplex-link-op $n13 $n11 orient right
#4rd block
$ns duplex-link-op $n5 $n14 orient left-down
$ns duplex-link-op $n14 $n15 orient right-down
$ns duplex-link-op $n15 $n16 orient left-down
$ns duplex-link-op $n16 $n17 orient left-up
$ns duplex-link-op $n17 $n14 orient right-up
#inside
$ns duplex-link-op $n14 $n16 orient down
$ns duplex-link-op $n17 $n15 orient right

#right side
$ns duplex-link-op $n0 $n18 orient right-down
$ns duplex-link-op $n18 $n19 orient right-down
$ns duplex-link-op $n19 $n20 orient right-down
$ns duplex-link-op $n20 $n21 orient left-down
$ns duplex-link-op $n21 $n22 orient left-up
$ns duplex-link-op $n22 $n19 orient right-up
#inside
$ns duplex-link-op $n19 $n21 orient down
$ns duplex-link-op $n22 $n20 orient right
#2nd block
$ns duplex-link-op $n21 $n23 orient down
$ns duplex-link-op $n23 $n24 orient right-down
$ns duplex-link-op $n24 $n25 orient left-down
$ns duplex-link-op $n25 $n26 orient left-up
$ns duplex-link-op $n26 $n23 orient right-up
#inside
$ns duplex-link-op $n23 $n25 orient down
$ns duplex-link-op $n26 $n24 orient right
#3rd block
$ns duplex-link-op $n20 $n27 orient right-down
$ns duplex-link-op $n27 $n28 orient right-down
$ns duplex-link-op $n28 $n29 orient left-down
$ns duplex-link-op $n29 $n30 orient left-up
$ns duplex-link-op $n30 $n27 orient right-up
#inside
$ns duplex-link-op $n27 $n29 orient down
$ns duplex-link-op $n30 $n28 orient right
#4rd block
$ns duplex-link-op $n22 $n31 orient left-down
$ns duplex-link-op $n31 $n32 orient right-down
$ns duplex-link-op $n32 $n33 orient left-down
$ns duplex-link-op $n33 $n34 orient left-up
$ns duplex-link-op $n34 $n31 orient right-up
#inside
$ns duplex-link-op $n31 $n33 orient down
$ns duplex-link-op $n34 $n32 orient right



proc finish {} {
	global ns f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 f13 f14 f15 f16 f17 f18 f19 f20 f21 f22 f23 f24 f25 f26 f27 f28 f29 f30 f31 f32 f33 f34
	
	$ns flush-trace 
	close $f0
	close $f1
	close $f2
	close $f3
	close $f4
	close $f5
	close $f6
	close $f7
	close $f8
	close $f9
	close $f10
	close $f11
	close $f12
	close $f13
	close $f14
	close $f15
	close $f16
	close $f17
	close $f18
	close $f19
	close $f20
	close $f21
	close $f22
	close $f23
	close $f24
	close $f25
	close $f26
	close $f27
	close $f28
	close $f29
	close $f30
	close $f31
	close $f32
	close $f33
	close $f34
	exec nam output34.nam &
	
	exec xgraph Cloud.tr Fog1.tr out2.tr out3.tr out4.tr out5.tr out6.tr out7.tr out8.tr out9.tr out10.tr out11.tr out12.tr out13.tr out14.tr out15.tr out16.tr out17.tr Fog2.tr out19.tr out20.tr out21.tr out22.tr out23.tr out24.tr out25.tr out26.tr out27.tr out28.tr out29.tr out30.tr out31.tr out32.tr out33.tr -geometry 800x400 &
        exit 0
}

proc attach-expoo-traffic { node sink size burst idle rate } {
	set ns [Simulator instance]
	set source [new Agent/UDP]
	$ns attach-agent $node $source

	set traffic [new Application/Traffic/Exponential]
	$traffic set packetSize_ $size
	$traffic set burst_time_ $burst
	$traffic set idle_time_ $idle
	$traffic set rate_ $rate
      
        $traffic attach-agent $source
        
	$ns connect $source $sink
	return $traffic
}

proc record {} {
        global sink0 sink1 sink2 sink3 sink4 sink5 sink6 sink7 sink8 sink9 sink10 sink11 sink12 sink13 sink14 sink15 sink16 sink17 sink18 sink19 sink20 sink21 sink22 sink23 sink24 sink25 sink26 sink27 sink28 sink29 sink30 sink31 sink32 sink33 f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12 f13 f14 f15 f16 f17 f18 f19 f20 f21 f22 f23 f24 f25 f26 f27 f28 f29 f30 f31 f32 f33

	set ns [Simulator instance]
        set time 0.5

        set bw0 [$sink0 set bytes_]
        set bw1 [$sink1 set bytes_]
        set bw2 [$sink2 set bytes_]
	set bw3 [$sink3 set bytes_]
        set bw4 [$sink4 set bytes_]
        set bw5 [$sink5 set bytes_]
	set bw6 [$sink6 set bytes_]
        set bw7 [$sink7 set bytes_]
        set bw8 [$sink8 set bytes_]
	set bw9 [$sink9 set bytes_]
        set bw10 [$sink10 set bytes_]
	set bw11 [$sink11 set bytes_]
        set bw12 [$sink12 set bytes_]
	set bw13 [$sink13 set bytes_]
        set bw14 [$sink14 set bytes_]
        set bw15 [$sink15 set bytes_]
	set bw16 [$sink16 set bytes_]
        set bw17 [$sink17 set bytes_]
        set bw18 [$sink18 set bytes_]
	set bw19 [$sink19 set bytes_]
        set bw20 [$sink20 set bytes_]
	set bw21 [$sink21 set bytes_]
        set bw22 [$sink22 set bytes_]
	set bw23 [$sink23 set bytes_]
        set bw24 [$sink24 set bytes_]
        set bw25 [$sink25 set bytes_]
	set bw26 [$sink26 set bytes_]
        set bw27 [$sink27 set bytes_]
        set bw28 [$sink28 set bytes_]
	set bw29 [$sink29 set bytes_]
        set bw30 [$sink30 set bytes_]
        set bw31 [$sink31 set bytes_]
        set bw32 [$sink32 set bytes_]
	set bw33 [$sink33 set bytes_]
	
        set now [$ns now]

        puts $f0 "$now [expr $bw0/$time*8/10000]"
        puts $f1 "$now [expr $bw1/$time*8/100000000]"
        puts $f2 "$now [expr $bw2/$time*8/1000000]"
	puts $f3 "$now [expr $bw3/$time*8/1000000]"
        puts $f4 "$now [expr $bw4/$time*8/1000000]"
        puts $f5 "$now [expr $bw5/$time*8/1000000]"
	puts $f6 "$now [expr $bw6/$time*8/1000000]"
        puts $f7 "$now [expr $bw7/$time*8/1000000]"
        puts $f8 "$now [expr $bw8/$time*8/1000000]"
	puts $f9 "$now [expr $bw9/$time*8/1000000]"
        puts $f10 "$now [expr $bw10/$time*8/1000000]"
        puts $f11 "$now [expr $bw11/$time*8/1000000]"
        puts $f12 "$now [expr $bw12/$time*8/1000000]"
	puts $f13 "$now [expr $bw13/$time*8/1000000]"
        puts $f14 "$now [expr $bw14/$time*8/1000000]"
        puts $f15 "$now [expr $bw15/$time*8/1000000]"
	puts $f16 "$now [expr $bw16/$time*8/1000000]"
        puts $f17 "$now [expr $bw17/$time*8/1000000]"
        puts $f18 "$now [expr $bw18/$time*8/100000000]"
	puts $f19 "$now [expr $bw19/$time*8/1000000]"
        puts $f20 "$now [expr $bw20/$time*8/1000000]"
        puts $f21 "$now [expr $bw21/$time*8/1000000]"
        puts $f22 "$now [expr $bw22/$time*8/1000000]"
	puts $f23 "$now [expr $bw23/$time*8/1000000]"
        puts $f24 "$now [expr $bw24/$time*8/1000000]"
        puts $f25 "$now [expr $bw25/$time*8/1000000]"
	puts $f26 "$now [expr $bw26/$time*8/1000000]"
        puts $f27 "$now [expr $bw27/$time*8/1000000]"
        puts $f28 "$now [expr $bw28/$time*8/1000000]"
	puts $f29 "$now [expr $bw29/$time*8/1000000]"
        puts $f30 "$now [expr $bw30/$time*8/1000000]"
        puts $f31 "$now [expr $bw31/$time*8/1000000]"
        puts $f32 "$now [expr $bw32/$time*8/1000000]"
	puts $f33 "$now [expr $bw33/$time*8/1000000]"
	
        $sink0 set bytes_ 512
        $sink1 set bytes_ 512
        $sink2 set bytes_ 512
	$sink3 set bytes_ 512
        $sink4 set bytes_ 512
        $sink5 set bytes_ 512
	$sink6 set bytes_ 512
        $sink7 set bytes_ 512
        $sink8 set bytes_ 512
	$sink9 set bytes_ 512
        $sink10 set bytes_ 512
        $sink11 set bytes_ 512
        $sink12 set bytes_ 512
	$sink13 set bytes_ 512
        $sink14 set bytes_ 512
        $sink15 set bytes_ 512
	$sink16 set bytes_ 512
        $sink17 set bytes_ 512
        $sink18 set bytes_ 512
	$sink19 set bytes_ 512
        $sink20 set bytes_ 512
        $sink11 set bytes_ 512
        $sink12 set bytes_ 512
	$sink13 set bytes_ 512
        $sink14 set bytes_ 512
        $sink15 set bytes_ 512
	$sink16 set bytes_ 512
        $sink17 set bytes_ 512
        $sink18 set bytes_ 512
	$sink19 set bytes_ 512
        $sink30 set bytes_ 512
        $sink31 set bytes_ 512
        $sink32 set bytes_ 512
	$sink33 set bytes_ 512
	
        $ns at [expr $now+$time] "record"
}

set sink0 [new Agent/LossMonitor]
set sink1 [new Agent/LossMonitor]
set sink2 [new Agent/LossMonitor]
set sink3 [new Agent/LossMonitor]
set sink4 [new Agent/LossMonitor]
set sink5 [new Agent/LossMonitor]
set sink6 [new Agent/LossMonitor]
set sink7 [new Agent/LossMonitor]
set sink8 [new Agent/LossMonitor]
set sink9 [new Agent/LossMonitor]
set sink10 [new Agent/LossMonitor]
set sink11 [new Agent/LossMonitor]
set sink12 [new Agent/LossMonitor]
set sink13 [new Agent/LossMonitor]
set sink14 [new Agent/LossMonitor]
set sink15 [new Agent/LossMonitor]
set sink16 [new Agent/LossMonitor]
set sink17 [new Agent/LossMonitor]
set sink18 [new Agent/LossMonitor]
set sink19 [new Agent/LossMonitor]
set sink20 [new Agent/LossMonitor]
set sink21 [new Agent/LossMonitor]
set sink22 [new Agent/LossMonitor]
set sink23 [new Agent/LossMonitor]
set sink24 [new Agent/LossMonitor]
set sink25 [new Agent/LossMonitor]
set sink26 [new Agent/LossMonitor]
set sink27 [new Agent/LossMonitor]
set sink28 [new Agent/LossMonitor]
set sink29 [new Agent/LossMonitor]
set sink30 [new Agent/LossMonitor]
set sink31 [new Agent/LossMonitor]
set sink32 [new Agent/LossMonitor]
set sink33 [new Agent/LossMonitor]

$ns attach-agent $n4 $sink0
$ns attach-agent $n4 $sink1
$ns attach-agent $n4 $sink2
$ns attach-agent $n4 $sink3
$ns attach-agent $n4 $sink4
$ns attach-agent $n4 $sink5
$ns attach-agent $n4 $sink6
$ns attach-agent $n4 $sink7
$ns attach-agent $n4 $sink8
$ns attach-agent $n4 $sink9
$ns attach-agent $n4 $sink10
$ns attach-agent $n4 $sink11
$ns attach-agent $n4 $sink12
$ns attach-agent $n4 $sink13
$ns attach-agent $n4 $sink14
$ns attach-agent $n4 $sink15
$ns attach-agent $n4 $sink16
$ns attach-agent $n4 $sink17
$ns attach-agent $n4 $sink18
$ns attach-agent $n4 $sink19
$ns attach-agent $n4 $sink20
$ns attach-agent $n4 $sink21
$ns attach-agent $n4 $sink22
$ns attach-agent $n4 $sink23
$ns attach-agent $n4 $sink24
$ns attach-agent $n4 $sink25
$ns attach-agent $n4 $sink26
$ns attach-agent $n4 $sink27
$ns attach-agent $n4 $sink28
$ns attach-agent $n4 $sink29
$ns attach-agent $n4 $sink30
$ns attach-agent $n4 $sink31
$ns attach-agent $n4 $sink32
$ns attach-agent $n4 $sink33

set source0 [attach-expoo-traffic $n0 $sink0 200 2s 1s 100k]
set source1 [attach-expoo-traffic $n1 $sink1 200 2s 1s 200k]
set source2 [attach-expoo-traffic $n2 $sink2 200 2s 1s 300k]
set source3 [attach-expoo-traffic $n3 $sink3 200 2s 1s 100k]
set source4 [attach-expoo-traffic $n4 $sink4 200 2s 1s 200k]
set source5 [attach-expoo-traffic $n5 $sink5 200 2s 1s 300k]
set source6 [attach-expoo-traffic $n6 $sink6 200 2s 1s 100k]
set source7 [attach-expoo-traffic $n7 $sink7 200 2s 1s 200k]
set source8 [attach-expoo-traffic $n8 $sink8 200 2s 1s 300k]
set source9 [attach-expoo-traffic $n9 $sink9 200 2s 1s 100k]
set source10 [attach-expoo-traffic $n10 $sink10 200 2s 1s 200k]
set source11 [attach-expoo-traffic $n11 $sink11 200 2s 1s 200k]
set source12 [attach-expoo-traffic $n12 $sink12 200 2s 1s 300k]
set source13 [attach-expoo-traffic $n13 $sink13 200 2s 1s 100k]
set source14 [attach-expoo-traffic $n14 $sink14 200 2s 1s 200k]
set source15 [attach-expoo-traffic $n15 $sink15 200 2s 1s 300k]
set source16 [attach-expoo-traffic $n16 $sink16 200 2s 1s 100k]
set source17 [attach-expoo-traffic $n17 $sink17 200 2s 1s 200k]
set source18 [attach-expoo-traffic $n18 $sink18 200 2s 1s 300k]
set source19 [attach-expoo-traffic $n19 $sink19 200 2s 1s 100k]
set source20 [attach-expoo-traffic $n20 $sink20 200 2s 1s 200k]
set source21 [attach-expoo-traffic $n21 $sink21 200 2s 1s 200k]
set source22 [attach-expoo-traffic $n22 $sink22 200 2s 1s 300k]
set source23 [attach-expoo-traffic $n23 $sink23 200 2s 1s 100k]
set source24 [attach-expoo-traffic $n24 $sink24 200 2s 1s 200k]
set source25 [attach-expoo-traffic $n25 $sink25 200 2s 1s 300k]
set source26 [attach-expoo-traffic $n26 $sink26 200 2s 1s 100k]
set source27 [attach-expoo-traffic $n27 $sink27 200 2s 1s 200k]
set source28 [attach-expoo-traffic $n28 $sink28 200 2s 1s 300k]
set source29 [attach-expoo-traffic $n29 $sink29 200 2s 1s 100k]
set source30 [attach-expoo-traffic $n30 $sink30 200 2s 1s 200k]
set source31 [attach-expoo-traffic $n31 $sink31 200 2s 1s 200k]
set source32 [attach-expoo-traffic $n32 $sink32 200 2s 1s 300k]
set source33 [attach-expoo-traffic $n33 $sink33 200 2s 1s 100k]

$ns at 0.0 "record"

$ns at 420.4412004 "$source0 start"
$ns at 419.4412004 "$source1 start"
$ns at 20.1812607 "$source2 start"
$ns at 27.6007499 "$source3 start"
$ns at 27.8248132 "$source4 start"
$ns at 28.561417 "$source5 start"
$ns at 38.8047405 "$source6 start"
$ns at 50.4569716 "$source7 start"
$ns at 57.6535253 "$source8 start"
$ns at 59.9889827 "$source9 start"
$ns at 61.0168276 "$source10 start"
$ns at 80.1940176 "$source11 start"
$ns at 80.8201374 "$source12 start"
$ns at 81.9459268 "$source13 start"
$ns at 82.1088105 "$source14 start"
$ns at 87.3101485 "$source15 start"
$ns at 99.7083185 "$source16 start"
$ns at 119.1404363 "$source17 start"
$ns at 425.7170028 "$source18 start"
$ns at 125.3242897 "$source19 start"
$ns at 128.6091205 "$source20 start"
$ns at 129.433748 "$source21 start"
$ns at 131.470639 "$source22 start"
$ns at 134.4228096 "$source23 start"
$ns at 135.3457177 "$source24 start"
$ns at 135.763269 "$source25 start"
$ns at 136.4029113 "$source26 start"
$ns at 136.8229631 "$source27 start"
$ns at 145.4438947 "$source28 start"
$ns at 145.6585188 "$source29 start"
$ns at 148.6015824 "$source30 start"
$ns at 154.8996756 "$source31 start"
$ns at 157.751152 "$source32 start"
$ns at 162.651352 "$source33 start"

$ns at 430.4412004 "$source0 stop"
$ns at 424.4412004 "$source1 stop"
$ns at 25.1812607 "$source2 stop"
$ns at 32.6007499 "$source3 stop"
$ns at 32.8248132 "$source4 stop"
$ns at 33.561417 "$source5 stop"
$ns at 42.8047405 "$source6 stop"
$ns at 55.4569716 "$source7 stop"
$ns at 62.6535253 "$source8 stop"
$ns at 64.9889827 "$source9 stop"
$ns at 66.0168276 "$source10 stop"
$ns at 85.1940176 "$source11 stop"
$ns at 85.8201374 "$source12 stop"
$ns at 86.9459268 "$source13 stop"
$ns at 87.1088105 "$source14 stop"
$ns at 92.3101485 "$source15 stop"
$ns at 104.7083185 "$source16 stop"
$ns at 124.1404363 "$source17 stop"
$ns at 429.7170028 "$source18 stop"
$ns at 130.3242897 "$source19 stop"
$ns at 133.6091205 "$source20 stop"
$ns at 134.433748 "$source21 stop"
$ns at 136.470639 "$source22 stop"
$ns at 139.4228096 "$source23 stop"
$ns at 140.3457177 "$source24 stop"
$ns at 140.763269 "$source25 stop"
$ns at 141.4029113 "$source26 stop"
$ns at 141.8229631 "$source27 stop"
$ns at 150.4438947 "$source28 stop"
$ns at 150.6585188 "$source29 stop"
$ns at 153.6015824 "$source30 stop"
$ns at 159.8996756 "$source31 stop"
$ns at 162.751152 "$source32 stop"
$ns at 167.651352 "$source33 stop"

$ns rtmodel-at 33.6007499 down $n3 $n10
$ns rtmodel-at 150.52 down $n0 $n18
$ns rtmodel-at 66.0168276 down $n23 $n25

$ns rtmodel-at 40.6007499 up $n1 $n2
$ns rtmodel-at 99.7083185 up $n16 $n17
$ns rtmodel-at 104.7083185 up $n19 $n21
$ns rtmodel-at 130.3242897 up $n34 $n32
#$ns rtmodel-at 43.52 up $n5 $n6

#$ns rtmodel-at 15.88 down $n5 $n14
#$ns rtmodel-at 3.52 up $n1 $n3

$ns at 500.0 "finish"

$ns run
