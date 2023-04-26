

Re-ID<br>
=====
<br><br>

<span style="white-space: pre-wrap" nonce="">There&#39;s some unrest in the minion ranks: minions with ID numbers like &quot;1&quot;, &quot;42&quot;, and other &quot;good&quot; numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new random IDs based on a Completely Foolproof Scheme. <br><br>Commander Lambda has concatenated the prime numbers in a single long string: &quot;2357111317192329...&quot;. Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion&#39;s new ID number will be the next five digits in the string. So if a minion draws &quot;3&quot;, their ID number will be &quot;71113&quot;. <br><br>Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda&#39;s string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.</span><br><br>

Languages<br>
=========<br><br>



To provide a Java solution, edit <span class="term-yellow">Solution.java</span><br>


To provide a Python solution, edit <span class="term-yellow">solution.py</span><br>


<br>
Test cases<br>
==========
<br>
Your code should pass the following test cases.<br>
Note that it may also be run against hidden test cases not shown here.<br><br>


	-- Java cases -- <br>

	

		
	

		
	

		
	

		
	

		
	

		
	

		
	

		
	

		
			

			Input:<br>

			Solution.solution(0)<br>

			
			Output:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;
			23571
			<br><br>
		
	

		
			

			Input:<br>

			Solution.solution(3)<br>

			
			Output:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;
			71113
			<br><br>
		
	

	-- Python cases -- <br>

	

		
	

		
	

		
			

			Input:<br>

			solution.solution(0)<br>

			
			Output:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;
			23571
			<br><br>
		
	

		
	

		
	

		
	

		
	

		
	

		
			

			Input:<br>

			solution.solution(3)<br>

			
			Output:<br>
			&nbsp;&nbsp;&nbsp;&nbsp;
			71113
			<br><br>
		
	

		
	


Use <span class="term-yellow">verify [file]</span> to test your solution and see how it does. When you are finished editing your code, use <span class="term-yellow">submit [file]</span> to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
