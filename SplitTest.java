import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

import java.awt.List;
import java.util.ArrayList;

import org.junit.jupiter.api.Test;
/**
 *
 * @author Marco Munoz
 * @version 1.0
 */

public class SplitTest {
	String str;
	int size;
	Split actual = new Split();

	@Test
	public void test1() {
		String output = actual.split("cs", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("c");
		expected.add("s");
		assertEquals(expected,output);

	}

	public void test2() {
		String output = actual.split(null, 2);
		fail("null is not a string");
	}

	public void test3() {
		String output = actual.split("cs rocks", 8);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("cs rocks");
		assertEquals(expected, output);
	}

	public void test4() {
		String output = actual.split("cs", 5);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("cs");
		assertEquals(expected, output);
	}
	public void test5() {
		String output = actual.split("cs",-1);
		fail("cannot split into negative numbers");

	}
	public void test6() {
		String output = actual.split("cs",0);
		fail("cannot split string by 0");
	}
	public void test7() {
		String output = actual.split("", 0);
		fail("empty string and cannot split by 0");
	}
	public void test8() {
		String output = actual.split("$", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("$");
		assertEquals(expected, output);
	}
	public void test9() {
		String output = actual.split("abc$", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("$");
		expected.add("b");
		expected.add("c");
		expected.add("$");
		assertEquals(expected, output);
	}
	public void test10() {
		String output = actual.split("+", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("+");
		assertEquals(expected, output);
	}
	public void test11() {
		String output = actual.split("-", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("-");
		assertEquals(expected, output);
	}
	public void test12() {
		String output = actual.split("/", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("/");
		assertEquals(expected, output);
	}
	public void test13() {
		String output = actual.split("*", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("*");
		assertEquals(expected, output);
	}
	public void test14() {
		String output = actual.split("!", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("!");
		assertEquals(expected, output);
	}
	public void test15() {
		String output = actual.split("++", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("+");
		expected.add("+");
		assertEquals(expected, output);
	}
	public void test16() {
		String output = actual.split("--", 1);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("-");
		expected.add("-");
		assertEquals(expected, output);
	}
	public void test17() {
		String output = actual.split("\n", 2);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("\n");
		assertEquals(expected, output);
	}
	public void test18() {
		String output = actual.split("\t", 2);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("\t");
		assertEquals(expected, output);
	}
	public void test19() {
		String output = actual.split("\\", 2);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("\\");
		assertEquals(expected, output);
	}
	public void test20() {
		String output = actual.split("\r", 2);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("\r");
		assertEquals(expected, output);
	}
	public void test21() {
		String output = actual.split(" ", 3);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add(" ");
		assertEquals(expected, output);
	}
	public void test22() {
		String output = actual.split("cs", 2147483647);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("cs");
		assertEquals(expected, output);
	}
	public void test23() {
		String output = actual.split("cs", -2147483648);
		ArrayList<String> expected = new ArrayList<String>();
		expected.add("cs");
		assertEquals(expected, output);
	}


// Test 24:
//	Actual: \b
//	Expected: "\b"
//	Size: 1

// Test 25:
//	Actual: /**
//	Expected: "/**"
//	Size: 1

// Test 26:
//	Actual: **/
//	Expected: "**/"
//	Size: 1

// Test 27:
//	Actual: String
//	Excpected: Exceptoin TypeError
//	Size: String

// Test 28:
//	Actual: (Int Value)
//	Expected: Exception TypeError
//	Size: 1

//	public void testExtra() {

//	}

}
