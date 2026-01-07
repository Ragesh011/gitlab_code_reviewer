# Java Coding Guidelines

**Purpose**: AI Reference for Java Code Review. Based on JetBrains Inspectopedia.
**Instructions**: Refer below rules while writing feedback review comments

## Abstraction Issues
*   **['instanceof' check for 'this']**: Reports usages of `instanceof` or `getClass()` checks on `this`, indicating inconsistent OO design.
*   **['Optional' used as field or parameter type]**: Reports usage of `java.util.Optional` as field/parameter types (it is not Serializable and meant for returns).
*   **['public' method not exposed in interface]**: Reports public methods not part of an implemented interface, affecting loose coupling.
*   **['public' method with 'boolean' parameter]**: Reports "boolean traps" in public APIs; confusing parameters should be enums or split methods.
*   **[Chain of 'instanceof' checks]**: Reports sequences of `if (obj instanceof A) ... else if (obj instanceof B)`, indicating missing polymorphism.
*   **[Class references one of its subclasses]**: Reports classes referencing their own subclasses, creating circular dependency and tight coupling.
*   **[Collection declared by class, not interface]**: Reports declarations using concrete types (e.g., `ArrayList`) instead of interfaces (e.g., `List`), limiting abstraction.
*   **[Feature envy]**: Reports methods making frequent calls (3+) to another class, suggesting functionality belongs there.
*   **[Interface method clashes with method in 'Object']**: Reports interface methods clashing with `Object.clone()` or `finalize()`, causing compilation or design issues.
*   **[Magic number]**: Reports numeric literals not defined as constants (excluding 0, 1, 2, etc.), leading to unclear code.
*   **[Overly strong type cast]**: Reports casting to a specific implementation (e.g., `ArrayList`) when an interface (e.g., `List`) would suffice.
*   **[Private method only used from inner class]**: Reports private methods used only by an inner class, suggesting they should be moved to that inner class.
*   **[Static member only used from one other class]**: Reports static members used only by one external class, suggesting they belong in that consuming class.
*   **[Type may be weakened]**: Reports variable/return types that are more specific than necessary, discouraging reusability (e.g., returning `ArrayList` instead of `List`).
*   **[Use of concrete class]**: Reports usages of concrete classes (e.g., in casts or parameters) instead of interfaces, hindering testing and abstraction.

## Assignment Issues
*   **['null' assignment]**: Reports variables assigned to `null` outside declarations, which can lead to NPEs. Use `Optional` or Sentinel objects instead.
*   **[Assignment can be replaced with operator assignment]**: Reports assignments like `x = x + 1` that can be replaced with `x += 1` for brevity and clarity.
*   **[Assignment to 'catch' block parameter]**: Reports assignments to `catch` parameters, which is confusing. Use a new variable instead.
*   **[Assignment to 'for' loop parameter]**: Reports modifications to `for` loop parameters inside the loop body, which is often a bug or confusing.
*   **[Assignment to lambda parameter]**: Reports modifications to lambda parameters, which may be a typo or confusing. Use a new local variable.
*   **[Assignment to method parameter]**: Reports assignments to method parameters, which can be confusing. Use `final` parameters or local variables.
*   **[Assignment to static field from instance context]**: Reports assignments to static fields from instance methods, risking unsafe shared state modification.
*   **[Assignment used as condition]**: Reports assignments in conditions (e.g., `if (a=b)`), which is often a typo for `==`.
*   **[Constructor assigns value to field defined in superclass]**: Reports subclass constructors assigning to superclass fields. Pass values to `super()` instead.
*   **[Nested assignment]**: Reports assignments nested in other expressions (e.g., `a = (b = c)`), reducing readability.
*   **[Result of '++' or '--' used]**: Reports increment/decrement used in expressions (e.g., `arr[i++]`), which can be confusing. Extract to separate statement.

## Bitwise Operation Issues
*   **[Incompatible bitwise mask operation]**: Reports bitwise expressions (e.g., `(var & 1) == 2`) that are logically impossible (always true or false).
*   **[Pointless bitwise expression]**: Reports redundant operations like `x | 0` or `x & -1`, which do nothing.
*   **[Shift operation by inappropriate constant]**: Reports shift amounts outside valid ranges (0-31 for int, 0-63 for long), which are likely errors.

## Class Metrics
*   **[Anonymous class with too many methods]**: Reports anonymous classes with excessive methods, suggesting they should be refactored into named inner classes.
*   **[Class too deep in inheritance tree]**: Reports classes with excessive inheritance depth, indicating complex hierarchy and potential design redundancy.
*   **[Class with too many constructors]**: Reports classes with too many constructors, which can lead to initialization errors; consider static factories or Builder pattern.
*   **[Class with too many fields]**: Reports classes with excessive fields, suggesting the class is doing too much (God Class) and should be split.
*   **[Class with too many methods]**: Reports classes with excessive methods, suggesting the class has too many responsibilities and should be split.
*   **[Inner class too deeply nested]**: Reports classes with excessive nesting of inner classes, making code confusing and hard to read.
*   **[Overly complex anonymous class]**: Reports anonymous classes with high cyclomatic complexity; they should be refactored into named classes.
*   **[Overly complex class]**: Reports classes with high total cyclomatic complexity, suggesting they should be split into smaller classes.
*   **[Overly coupled class]**: Reports classes that reference too many other classes, indicating high coupling and fragility.

## Class Structure
*   **['private' method declared 'final']**: Reports `final` modifier on `private` methods as redundant (private methods cannot be overridden).
*   **['public' constructor can be replaced with factory method]**: Reports public constructors, suggesting static factory methods for better flexibility.
*   **['static' method declared 'final']**: Reports `final` modifier on `static` methods as redundant (static methods cannot be overridden).
*   **['static', non-'final' field]**: Reports `static` fields that are not `final`, representing unsafe global mutable state.
*   **[Abstract 'class' may be 'interface']**: Reports abstract classes with no state/implementation that can be converted to interfaces.
*   **[Anonymous class can be replaced with inner class]**: Reports anonymous classes that should be promoted to named inner classes for readability.
*   **[Class is closed to inheritance]**: Reports `final` classes (not sealed), which limit extensibility and Object-Oriented design.
*   **[Class may extend adapter instead of implementing listener]**: Reports classes implementing listeners directly instead of extending adapters (which provides default implementations).
*   **[Class name differs from file name]**: Reports top-level class names differing from file names, which violates Java conventions and tooling expectations.
*   **[Class with only 'private' constructors should be declared 'final']**: Reports classes with only private constructors that are not `final`; they cannot be extended, so they should be final.
*   **[Constant declared in 'abstract' class]**: Reports constants in abstract classes, suggesting they might be better placed in interfaces.
*   **[Constant declared in interface]**: Reports constants in interfaces, suggesting they might be better placed in abstract classes (depends on standard).
*   **[Empty class]**: Reports empty classes with no members, often leftovers from refactoring.
*   **[Field can be local variable]**: Reports fields that are only used locally within methods, suggesting they should be converted to local variables.
*   **[Inner class of interface]**: Reports inner classes within interfaces, which can be confusing and discouraged.
*   **[Interface may be annotated as '@FunctionalInterface']**: Reports interfaces matching the Functional Interface contract but missing the annotation.
*   **[Local class]**: Reports local classes (nested in blocks), which are uncommon and can be confusing.
*   **[Marker interface]**: Reports interfaces with no methods/fields, which are often design failures (use Annotations instead).
*   **[Method can't be overridden]**: Reports methods declared `final`, which limits extensibility and mocking in tests.
*   **[Method returns per-class constant]**: Reports methods returning constants that vary by class, suggesting field-based configuration instead.
*   **[Multiple top level classes in single file]**: Reports multiple top-level classes in one file, which is confusing and non-standard.
*   **[No-op method in 'abstract' class]**: Reports empty methods in abstract classes; they should likely be `abstract` to force implementation.
*   **[Non-'static' initializer]**: Reports instance initializers (blocks), suggesting constructors or field initializers are clearer.
*   **[Non-final field in 'enum']**: Reports mutable fields in enums, which introduces unsafe global state.
*   **[Singleton]**: Reports Singleton pattern usage, which can hinder testing and OO design (consider Dependency Injection).
*   **[Utility class]**: Reports utility classes (static methods only), which may indicate procedural programming (Object-Oriented design is preferred).
*   **[Utility class can be 'enum']**: Reports utility classes that could be enums to enforce the "no instance" pattern essentially.
*   **[Utility class with 'public' constructor]**: Reports utility classes with public constructors, permitting instantiation; use private constructors instead.
*   **[Utility class without 'private' constructor]**: Reports utility classes without private constructors, allowing default public ones; add a private constructor.
*   **[Value passed as parameter never read]**: Reports parameters that are overwritten before being read, indicating redundancy or errors.

## Cloning Issues
*   **['clone()' does not declare 'CloneNotSupportedException']**: Reports `clone()` methods missing `throws CloneNotSupportedException`, which breaks standard cloning contracts.
*   **['clone()' instantiates objects with constructor]**: Reports `clone()` calling constructors instead of `super.clone()`, breaking subclass cloning.
*   **['clone()' method in non-Cloneable class]**: Reports `clone()` overrides in classes not implementing `Cloneable`, which is a logic error.
*   **['clone()' method not 'public']**: Reports `protected` `clone()` methods, recommending they be `public` for usability.
*   **['clone()' should have return type equal to the class it contains]**: Reports `clone()` returning `Object` instead of the specific class type (covariant return).
*   **[Cloneable class without 'clone()' method]**: Reports `Cloneable` classes missing `clone()` override, which defaults to protected `Object.clone()`.
*   **[Use of 'clone()' or 'Cloneable']**: Reports any use of `clone()`/`Cloneable`, as copy constructors or factories are often preferred.

## Code Maturity
*   **['Throwable' printed to 'System.out']**: Reports `System.out.println(e)`, recommending Logger use instead for proper stack trace handling.
*   **[Call to 'printStackTrace()']**: Reports `e.printStackTrace()`, which prints to stderr; recommend Logger for production code.
*   **[Call to 'Thread.dumpStack()']**: Reports `Thread.dumpStack()`, typically used for debug; remove or replacement with Logger.
*   **[Commented out code]**: Reports blocks of commented-out code, which should be removed (rely on Git history).
*   **[Deprecated API usage]**: Reports use of deprecated APIs, suggesting migration to recommended alternatives.
*   **[Deprecated member is still used]**: Reports deprecated members (fields/methods) still used within the same project code.
*   **[Method can be extracted]**: Suggests massive methods or complex blocks that could be extracted into smaller methods for readability.
*   **[Null value for Optional type]**: Reports `null` assigned to/returned as `Optional`; use `Optional.empty()` to avoid NPEs.
*   **[Redundant @ScheduledForRemoval annotation]**: Reports redundant usage of `@ApiStatus.ScheduledForRemoval` when `@Deprecated(forRemoval=true)` suffices.
*   **[Usage of API marked for removal]**: Reports methods/classes marked `@Deprecated(forRemoval=true)`; highly critical to fix before upgrade.
*   **[Use of 'System.out' or 'System.err']**: Reports direct stdout/stderr usage; recommend Logger for controlled output.
*   **[Use of obsolete collection type]**: Reports `Vector`/`Hashtable`/`Stack`; recommend `ArrayList`/`HashMap`/`Deque` (or `Concurrent...`).
*   **[Use of obsolete date-time API]**: Reports `java.util.Date`/`Calendar`; recommend usage of `java.time` (JSR-310).

## Code Style
*   **['assert' message is not a string]**: Reports `assert` messages that are not strings (e.g., boolean), which provide poor diagnostic info.
*   **['equals()' called on enum value]**: Reports `enum.equals()`, suggesting `==` for identity comparison (safer and clearer for enums).
*   **['if' statement can be replaced with conditional or boolean expression]**: Suggests simplifying `if` statements into `&&`, `||`, or ternary `?:` expressions.
*   **['List.indexOf()' expression can be replaced with 'contains()']**: Reports `indexOf() > -1` checks, recommending `contains()` for readability.
*   **['Objects.equals()' can be replaced with 'equals()']**: Reports `Objects.equals(a, b)` where `a` is known non-null; suggests `a.equals(b)` or `==` (primitives).
*   **['Optional' can be replaced with sequence of 'if' statements]**: Reports complex `Optional` chains that might be clearer as simple `if` checks (downgrading).
*   **['Optional' contains array or collection]**: Reports `Optional<List>`, suggesting empty collections instead of `Optional` wrappers.
*   **['return' separated from the result computation]**: Suggests moving `return` closer to computation or inlining variables for cleaner logic flow.
*   **['size() == 0' can be replaced with 'isEmpty()']**: Reports `size() == 0`, recommending `.isEmpty()` for collections/maps/strings (more readable/efficient).
*   **['try' statement with multiple resources can be split]**: Suggests splitting multi-resource `try` blocks for granular exception handling or refactoring.
*   **[Array can be replaced with enum values]**: Reports arrays of enum constants, suggesting `Enum.values()` to avoid manual maintenance.
*   **[Array creation without 'new' expression]**: Reports array initializers without `new` keyword (e.g., `int[] a = {1}`), suggesting explicit creation for consistency.
*   **[Assignment can be joined with declaration]**: Reports `int x; x = 5;`, suggesting `int x = 5;` for conciseness.
*   **[Block marker comment]**: Reports comments used as block markers (e.g., `// end if`), which are clutter; recommend removing.
*   **[C-style array declaration]**: Reports `int a[]`, recommending `int[] a` (Java style) for consistency.
*   **[Call to 'String.concat()' can be replaced with '+']**: Reports `str.concat("a")`, suggesting `str + "a"` for standard readability.
*   **[Can use bounded wildcard]**: Reports generic parameters that could use `? extends/super T` to increase API flexibility (PECS principle).
*   **[Chained equality comparisons]**: Reports `a == b == c` (confusing precedence), suggesting `a == b && b == c` or parentheses.
*   **[Chained method calls]**: Reports long method chains, suggesting breaking them with intermediate variables for debugging/readability.
*   **[Class explicitly extends 'Object']**: Reports `class A extends Object`, which is redundant; recommend removing `extends Object`.
*   **[Code block contains single statement]**: Reports single-statement blocks `{ stmt; }`, suggesting removing braces (unless style enforces them).
*   **[Conditional can be replaced with Optional]**: Reports `if (x != null)` patterns, suggesting `Optional` chains (may change semantics).
*   **[Confusing octal escape sequence]**: Reports octal escapes like `\123`, which are easily misread; recommend clear unicodes or standard escapes.
*   **[Constant expression can be evaluated]**: Reports static constants like `2 + 2`, suggesting modification to the calculated value.
*   **[Constant on wrong side of comparison]**: Reports constants on the "wrong" side (e.g., `var.equals("const")`), enforcing a consistent style (e.g., Yoda or not).
*   **[Control flow statement without braces]**: Reports control flow (if/for/while) without braces, enforcing `{}` for safety ("goto fail" protection).
*   **[Diamond can be replaced with explicit type arguments]**: Reports diamond `<>` usage, suggesting explicit types (useful for compatibility/downgrading).
*   **[Field assignment can be moved to initializer]**: Reports constructor assignments to fields that could be in the declaration; recommend moving for cleaner constructors.
*   **[Field may be 'final']**: Reports effectively final fields, recommending the `final` modifier for immutability info.
*   **[Implicit call to 'super()']**: Reports missing `super()` in constructors; recommend explicit call for clarity/style.
*   **[Instance field access not qualified with 'this']**: Reports field usage without `this.`, enforcing `this.field` style.
*   **[Instance method call not qualified with 'this']**: Reports method usage without `this.`, enforcing `this.method()` style.
*   **[Labeled switch rule can have code block]**: Reports switch rules like `case -> expr;`, suggesting wrapping in `{}`.
*   **[Labeled switch rule has redundant code block]**: Reports `case -> { expr; }`, suggesting `case -> expr;` for conciseness.
*   **[Lambda body can be code block]**: Reports `x -> expr`, suggesting `x -> { return expr; }`.
*   **[Lambda can be replaced with anonymous class]**: Reports lambdas, suggesting anonymous classes (downgrade or specific need).
*   **[Lambda parameter type can be specified]**: Reports inferred types `x ->`, suggesting explicit types `(String x) ->`.
*   **[Local variable or parameter can be 'final']**: Reports effectively final locals/params, recommending `final`.
*   **[Method reference can be replaced with lambda]**: Reports `String::length`, suggesting `s -> s.length()` (consistency).
*   **[Missorted modifiers]**: Reports modifiers out of order (e.g., `final static public`), enforcing JLS order (`public static final`).
*   **[Multi-catch can be split into separate catch blocks]**: Reports multi-catch `try { } catch (A | B e) ...`, suggesting splitting for specific handling.
*   **[Multiple operators with different precedence]**: Reports `a && b || c` without parentheses, enforcing explicit precedence for clarity.
*   **[Multiple variables in one declaration]**: Reports `int x, y;`, enforcing one variable per declaration `int x; int y;`.
*   **[Nested method call]**: Reports deeply nested calls `f(g(h()))`, suggesting intermediate variables for debugging.
*   **[Non functional style 'Optional.isPresent()' usage]**: Reports `if (opt.isPresent()) ...`, suggesting `opt.ifPresent(...)` or `map`.
*   **[Non-normalized annotation]**: Reports `@Annotation(value="foo")`, suggesting `@Annotation("foo")` (shorthand).
*   **[Non-terminal use of '\s' escape sequence]**: Reports `\s` (space) usage outside text block line ends, which might be confusing vs ` `.
*   **[Reassigned variable]**: Reports variables assigned multiple times, suggesting splitting/final vars (SSA form).
*   **[Record can be converted to class]**: Reports records, suggesting conversion to classes (downgrade).
*   **[Redundant 'new' expression in constant array creation]**: Reports `new int[]{1, 2}`, suggesting `{1, 2}` in initializers.
*   **[Redundant field initialization]**: Reports explicit initialization to default values (e.g., `int x = 0;`), suggesting removal.
*   **[Redundant no-arg constructor]**: Reports default constructors that are empty and redundant (compiler generates them).
*   **[Return of 'this']**: Reports `return this;`, usually part of chained setters; some styles ban this for clarity vs chaining.
*   **[Same file subclasses are missing from permits clause of a sealed class]**: Reports sealed classes without `permits` (if subclasses are in the same file); optional but explicit `permits` may be preferred.
*   **[Simplifiable annotation]**: Reports redundant annotation syntax (e.g., `@A(value="b")` -> `@A("b")`), suggesting simplification.
*   **[Standard 'Charset' object can be used]**: Reports `Charset.forName("UTF-8")`, suggesting `StandardCharsets.UTF_8` (faster, safer).
*   **[Stream API call chain can be replaced with loop]**: Reports streams that can be loops (useful for downgrading or performance tweaks).
*   **[String literal may be 'equals()' qualifier]**: Reports `str.equals("lit")`, suggesting `"lit".equals(str)` to avoid NPE (Yoda condition).
*   **[Subsequent steps can be fused into Stream API chain]**: Reports post-stream steps (e.g., `list.add`) that can be part of the stream (`.collect()`).
*   **[Trailing whitespace in text block]**: Reports trailing whitespace in Java 15 text blocks (stripped by compiler, but might be confusing).
*   **[Type parameter explicitly extends 'Object']**: Reports `T extends Object`, which is redundant (all objects extend Object).
*   **[Unnecessary conversion to 'String']**: Reports `String.valueOf(s)` in concatenations (e.g., `"" + s`), suggesting simplification.
*   **[Unnecessary fully qualified name]**: Reports `java.util.List` when `List` is imported/available, suggesting shortening.
*   **[Unnecessary Javadoc link]**: Reports `@link` to self/super methods that are redundant.
*   **[Unnecessary parentheses]**: Reports `(a + b)` where valid without, suggesting removal for clutter reduction.
*   **[Unnecessary qualifier for 'this' or 'super']**: Reports `this.method()` where unambiguous; suggests removal (note: conflicts with 'Unqualified access' rules).
*   **[Method name same as class name]**: Reports methods named same as class (not constructors), suggesting renaming to avoid confusion.
*   **[Unnecessarily qualified inner class access]**: Reports `Outer.Inner` inside `Outer` context, suggesting shortening to `Inner`.
*   **[Unnecessarily qualified static access]**: Reports `Class.staticMeth()` when imported statically or in same class, suggesting shortening.
*   **[Unnecessary call to 'toString()']**: Reports `obj.toString()` in concatenations (e.g., `"s" + obj.toString()`), suggesting removal (handled implicitly).
*   **[Unnecessary modifier]**: Reports redundant modifiers (e.g., `public` in interface methods), suggesting removal.
*   **[Unnecessary semicolon]**: Reports redundant semicolons (e.g., after `}`), suggesting removal.
*   **[Unnecessary temporary object in conversion from/to 'String']**: Reports inefficient String conversions (e.g., `new String(int).toString()`), suggesting optimized alternatives.
*   **[Unnecessary unary minus]**: Reports `- -x` or similar, suggesting simplification.

## Compiler Issues
*   **[Javac quirks]**: Reports known Javac compiler bugs or strictness issues (e.g., generic array creation quirks).
*   **[Preview Feature warning]**: Reports usage of Java Preview Features (marked `@PreviewFeature`), indicating unstable APIs.
*   **[Unchecked warning]**: Reports code causing `javac` unchecked warnings (raw types, unchecked casts), preventing compile-time type safety.
*   **[Value-based warnings]**: Reports synchronization on value-based classes (e.g., `Integer`), which is invalid in modern Java.

## Concurrency Annotation Issues
*   **[Instance member guarded by static field]**: Reports `@GuardedBy("staticField")` on instance members; mismatch in scope (static guard for instance).
*   **[Non-final '@GuardedBy' field]**: Reports non-final fields used as locks in `@GuardedBy`; locks should be stable (`final`).
*   **[Non-final field in '@Immutable' class]**: Reports mutable (non-final) fields in classes marked `@Immutable`; violates immutability contract.
*   **[Static member guarded by instance field or this]**: Reports `@GuardedBy("instanceField")` on static members; static members need static guards.
*   **[Unguarded field access or method call]**: Reports access to `@GuardedBy` fields without holding the specified lock.
*   **[Unknown '@GuardedBy' field]**: Reports `@GuardedBy("unknown")` where the lock field doesn't exist.

## Control Flow Issues
*   **['break' statement]**: Reports `break` statements outside of `switch` (e.g., in loops), complicating refactoring.
*   **['break' statement with label]**: Reports labeled `break` statements, which can be confusing and mimic `goto`.
*   **['continue' statement]**: Reports `continue` statements, suggesting rewriting loop logic for clarity.
*   **['continue' statement with label]**: Reports labeled `continue` statements, which complicate control flow.
*   **['default' not last case in 'switch']**: Reports `switch` statements where `default` is not the last branch.
*   **['for' loop may be replaced by 'while' loop]**: Reports `for` loops without init/update components; suggests using `while`.
*   **['for' loop with missing components]**: Reports `for` loops missing init/condition/update; suggests `while` or proper `for`.
*   **['if' statement with identical branches or common parts]**: Reports `if` branches with identical code or common tail portions; suggests extraction.
*   **['if' statement with negated condition]**: Reports `if (!cond) ... else ...`, suggesting swapping branches for better readability.
*   **['if' statement with too many branches]**: Reports `if/else if` chains with excessive branches; suggests `switch` or polymorphism.
*   **['switch' statement]**: Reports `switch` statements; some consider them poor OO design (replace with polymorphism).
*   **['switch' statement with too low of a branch density]**: Reports `switch` with few branches/lines; suggests `if/else` or refactoring.
*   **['switch' statement without 'default' branch]**: Reports `switch` missing `default`, risking unhandled cases.
*   **['while' can be replaced with 'do while']**: Reports `while` loops with duplicated code before loop; suggests `do-while`.
*   **[Assertion can be replaced with 'if' statement]**: Reports `assert` (often disabled in prod); suggests explicit `if` throwing `AssertionError`.
*   **[Boolean expression can be replaced with conditional expression]**: Reports boolean logic that's clearer as ternary/conditional.
*   **[Common subexpression can be extracted from 'switch']**: Reports duplicated code in all `switch` branches; suggests extraction.
*   **[Conditional break inside loop]**: Reports conditional `break` at start/end of loop; suggests moving condition to loop header.
*   **[Conditional can be pushed inside branch expression]**: Reports `if (cond) a=x else a=y` patterns; suggests `a = cond ? x : y`.
*   **[Conditional expression]**: Reports usage of ternary operator (`? :`); some styles prohibit it for clarity.
*   **[Conditional expression with identical branches]**: Reports `cond ? x : x`, indicating a bug or redundancy.
*   **[Conditional expression with negated condition]**: Reports `!cond ? x : y`, suggesting swapping branches for clarity.
*   **[Constant conditional expression]**: Reports `true ? x : y` or similar, suggesting simplification.
*   **[Double negation]**: Reports `!!x` or `!(!x == y)`, suggesting simplification.
*   **[Duplicate condition]**: Reports `cond && cond` or similar in `if`/`while`, suggesting a bug.
*   **[Enum 'switch' statement that misses case]**: Reports non-exhaustive `switch` on enums; suggests adding cases or `default`.
*   **[Expression can be factorized]**: Reports `(a && b) || (a && c)`; suggests `a && (b || c)` for readability.
*   **[Fallthrough in 'switch' statement]**: Reports missing `break` in `switch` cases, risking unintended execution.
*   **[Idempotent loop body]**: Reports loops that don't change state after the first iteration, indicating a probable bug.
*   **[Labeled statement]**: Reports labeled statements, which complicate refactoring and control flow logic.
*   **[Local variable used and declared in different 'switch' branches]**: Reports confusing variable scope across `switch` branches.
*   **[Loop statement that does not loop]**: Reports loops (`for`, `while`, `do`) that execute at most once, indicating a probable bug.
*   **[Loop variable not updated inside loop]**: Reports loop variables used in condition but not updated, risking infinite loops.
*   **[Loop with implicit termination condition]**: Reports `while(true)` with an `if(break)`; suggests moving the condition to the loop header.
*   **[Maximum 'switch' branches]**: Reports `switch` statements with excessive cases, suggesting refactoring or redesign.
*   **[Minimum 'switch' branches]**: Reports `switch` statements with too few cases (e.g., < 3); suggests `if`/`else if` chains.
*   **[Negated conditional expression]**: Reports `!(cond) ? x : y`, suggesting propagating the negation or swapping branches.
*   **[Negated equality expression]**: Reports `!(x == y)`, suggesting simplification to `x != y`.
*   **[Nested 'switch' statement]**: Reports nested `switch` statements, which are highly confusing; suggests method extraction.
*   **[Nested conditional expression]**: Reports nested ternary operators, which reduce readability; suggests `if`/`else`.
*   **[Overly complex boolean expression]**: Reports boolean expressions with too many terms (e.g., > 3), suggesting simplification.
*   **[Pointless 'indexOf()' comparison]**: Reports `indexOf` comparisons (e.g., `idx < -1`) that are always true/false.
*   **[Pointless boolean expression]**: Reports meaningless operations like `x && true` or `x || false`.
*   **[Redundant 'else']**: Reports `else` blocks after strict control flow (return/break), suggesting line simplification.
*   **[Redundant 'if' statement]**: Reports `if (cond) return true; else return false;` which can be `return cond;`.
*   **[Simplifiable boolean expression]**: Reports boolean logic that can be reduced (e.g., De Morgan's laws).
*   **[Simplifiable conditional expression]**: Reports `cond ? true : false` which is just `cond`.
*   **[Statement can be replaced with 'assert' or 'Objects.requireNonNull']**: Reports manual checks definable as assertions or standard null checks.

## Data Flow Issues
*   **[Boolean method is always inverted]**: Reports methods always called with `!method()`; suggests renaming (e.g., `isNotX` -> `isX`).
*   **[Boolean variable is always inverted]**: Reports booleans always used as `!var`; suggests inverting logic and renaming.
*   **[Law of Demeter]**: Reports violations (method chains `a.getB().getC()`), indicating tight coupling.
*   **[Negatively named boolean variable]**: Reports negative names (e.g., `isDisabled`); suggests positive names (`isEnabled`) for clarity.
*   **[Redundant local variable]**: Reports variables immediately returned or redundant; suggests inlining.
*   **[Reuse of local variable]**: Reports variables reused for unrelated purposes; suggests separate variables for clarity.
*   **[Scope of variable is too broad]**: Reports variables declared in outer scope but only used in inner; suggests narrowing scope.
*   **[Use of variable whose value is known to be constant]**: Reports variables that are effectively constant; suggests using the constant directly.

## Dependency Issues
*   **[Class with too many dependencies]**: Reports high fan-out (coupling); suggests decoupling.
*   **[Class with too many dependents]**: Reports high fan-in; suggests splitting or abstraction.
*   **[Class with too many transitive dependencies]**: Reports deep dependency trees, indicating complexity.
*   **[Class with too many transitive dependents]**: Reports deep dependent trees, indicating broad impact of changes.
*   **[Cyclic class dependency]**: Reports `A -> B -> A` cycles; critical design flaw.
*   **[Cyclic package dependency]**: Reports package-level cycles; suggests moving classes or splitting packages.

## Declaration Redundancy
*   **['final' method in 'final' class]**: Reports redundant `final` modifier on methods within `final` classes.
*   **['protected' member in 'final' class]**: Reports `protected` members in `final` classes; suggests `private` or package-private.
*   **[@SafeVarargs is not applicable to reifiable types]**: Reports redundant `@SafeVarargs` on methods with reifiable variable arity types.
*   **[Access static member via instance reference]**: Reports access to static members via instances (e.g., `obj.staticField`); suggests `Class.staticField`.
*   **[Declaration access can be weaker]**: Reports members with broader access than instantiated; suggests narrowing (e.g., `public` -> `private`).
*   **[Declaration can have 'final' modifier]**: Reports fields/methods/classes that can be `final` for immutability and design clarity.
*   **[Default annotation parameter value]**: Reports redundant explicit assignment of default values in annotations.
*   **[Duplicate throws]**: Reports duplicate exception types in a method's `throws` clause.
*   **[Empty class initializer]**: Reports empty `static {}` blocks, suggesting removal.
*   **[Functional expression can be folded]**: Reports lambdas that can be replaced by method references or qualifiers to reduce allocation.
*   **[Java module definition problems]**: Reports issues in `module-info.java` (e.g., provided but unused services).
*   **[Method always returns the same value]**: Reports methods returning a constant; suggests simplification or making `void` if return ignored.
*   **[Method can be made 'void']**: Reports methods whose return values are never used; suggests changing return type to `void`.
*   **[Method parameter always has the same value]**: Reports parameters always passed the same constant; suggests removing parameter or inlining.
*   **[Redundant 'close()']**: Reports unnecessary `close()` calls in try-with-resources blocks.
*   **[Redundant 'requires' directive in module-info]**: Reports unused module dependencies in `module-info.java`.
*   **[Redundant 'throws' clause]**: Reports exceptions declarations that are never thrown by the method.
*   **[Redundant lambda parameter types]**: Reports explicit types in lambdas that can be inferred (redundant).
*   **[Redundant record constructor]**: Reports unnecessary constructors in Java Records.
*   **[Unnecessary module dependency]**: Reports unused module dependencies; suggests removal.
*   **[Unused declaration]**: Reports classes/methods/fields/parameters that are implicitly or explicitly unused.
*   **[Unused label]**: Reports labels that are not targets of any `break` or `continue` statement.
*   **[Unused library]**: Reports libraries attached to the project but unused in code.

## Encapsulation Issues
*   **['public' field]**: Reports public fields (except static final); suggests using `private` fields with accessors.
*   **['public' nested class]**: Reports public nested classes; suggests reducing scope to `package-private` or `private`.
*   **[Accessing a non-public field of another object]**: Reports direct access to non-public fields of other objects.
*   **[Assignment or return of field with mutable type]**: Reports exposing mutable fields (e.g., `Date`, `Collection`); suggests returning defensive copies.
*   **[Package-visible field]**: Reports package-private fields; suggests `private` for better encapsulation.
*   **[Package-visible nested class]**: Reports package-private nested classes; suggests `private` if used only within the class.
*   **[Protected field]**: Reports `protected` fields; suggests `private` fields with getters/setters.
*   **[Protected nested class]**: Reports `protected` nested classes; suggests `private` if not accessed by subclasses.

## Finalization Issues
*   **['finalize()' called explicitly]**: Reports explicit usage of `finalize()`, which is usually an error.
*   **['finalize()' should be protected, not public]**: Reports `public finalize()`; specs require it to be `protected`.
*   **['finalize()' should not be overridden]**: Reports overriding `finalize()`, which is unpredictable and deprecated; suggests `AutoCloseable`.

## Error Handling
*   **['continue' or 'break' inside 'finally' block]**: Reports control flow escaping `finally`, which can suppress exceptions.
*   **['Error' not rethrown]**: Reports catching `java.lang.Error` without rethrowing; errors are usually unrecoverable.
*   **['finally' block which can not complete normally]**: Reports abrupt completion (`return`, `throw`) in `finally`; masks exceptions.
*   **['instanceof' on 'catch' parameter]**: Reports type checks on caught exceptions; suggests separate `catch` blocks.
*   **['null' thrown]**: Reports `throw null`, which causes `NullPointerException` instead of the intended logic.
*   **['return' inside 'finally' block]**: Reports `return` in `finally`, which discards any exception thrown in `try` block.
*   **['ThreadDeath' not rethrown]**: Reports catching `ThreadDeath` without rethrow, preventing thread termination.
*   **['throw' caught by containing 'try' statement]**: Reports `throw` used for local control flow; suggests refactoring.
*   **['throw' inside 'catch' block which ignores the caught exception]**: Reports rethrowing without chaining the original cause (lost context).
*   **['throw' inside 'finally' block]**: Reports `throw` in `finally`, masking the original exception.
*   **[Catch block may ignore exception]**: Reports ignored exceptions; suggests logging or valid suppression (e.g., `ignored` var name).
*   **[Caught exception is immediately rethrown]**: Reports `catch (E e) { throw e; }`; suggests removing the redundant catch.
*   **[Checked exception class]**: Reports custom exceptions extending `Exception`; generally, `RuntimeException` is preferred in modern Java.
*   **[Class directly extends 'Throwable']**: Reports extending `Throwable`; suggests extending `Exception` or `RuntimeException`.
*   **[Empty 'finally' block]**: Reports empty `finally` blocks, which are redundant.
*   **[Empty 'try' block]**: Reports empty `try` blocks, which are redundant.
*   **[Exception constructor called without arguments]**: Reports exception thrown without a message; suggests providing context.
*   **[Nested 'try' statement]**: Reports nested `try` blocks; suggests merging for clarity.
*   **[Non-final field of 'Exception' class]**: Reports mutable fields in exceptions; suggests `final` to preserve context snapshot.
*   **[Overly broad 'throws' clause]**: Reports `throws` clauses more generic than actual exceptions (e.g., `throws Exception`); suggests narrowing.
*   **[Prohibited 'Exception' caught]**: Reports catching specific prohibited exceptions (e.g., `NullPointerException`), which usually mask bugs.
*   **[Prohibited exception declared]**: Reports declaring prohibited exceptions (e.g., `throws Throwable`); suggests specific exceptions.
*   **[Prohibited exception thrown]**: Reports throwing prohibited exceptions (e.g., `throw new Exception()`); suggests custom or specific exceptions.
*   **[Throwable supplier never returns a value]**: Reports `Optional.orElseThrow(() -> { throw e; })`; suggests `Optional.orElseThrow(Ex::new)`.
*   **[Unchecked 'Exception' class]**: Reports subclasses of `RuntimeException`; useful if policy requires checked exceptions.
*   **[Unchecked exception declared in 'throws' clause]**: Reports `throws RuntimeException`; unchecked exceptions need not be declared.

## Imports
*   **['*' import]**: Reports on-demand imports (`import java.util.*`); suggests explicit imports (`import java.util.List`) to prevent conflicts.
*   **[Missorted imports]**: Reports imports not following the project's sort order; suggests sorting.
*   **[Single class import]**: Reports single-class imports if on-demand is configured (usually, explicit imports are preferred).
*   **[Static import]**: Reports static imports, which can sometimes make code harder to read; use judiciously.
*   **[Static import can be used based on the auto-import table]**: Reports qualified access that can be replaced by static imports for brevity.
*   **[Unnecessary import from the 'java.lang' package]**: Reports imports from `java.lang` (implicitly imported); suggests removal.
*   **[Unnecessary import from the same package]**: Reports imports of classes in the same package; suggests removal.
*   **[Unused import]**: Reports imports that are not used; suggests removal.

## Initialization Issues
*   **['this' reference escaped in object construction]**: Reports escaping `this` in constructors (e.g., passing to another object); causes thread-safety issues.
*   **[Abstract method called during object construction]**: Reports calls to abstract methods in constructors; leads to runtime errors if subclasses aren't initialized.
*   **[Double brace initialization]**: Reports double brace init (`new ArrayList() {{ ... }}`); creates unnecessary anonymous classes.
*   **[Instance field may not be initialized]**: Reports fields that might remain null/uninitialized after construction.
*   **[Instance field used before initialization]**: Reports usage of fields before they are assigned.
*   **[Non-final static field is used during class initialization]**: Reports reading non-final statics in `static {}`; unpredictable order.
*   **[Overridable method called during object construction]**: Reports calls to overridable methods in constructors; execution runs before subclass init.
*   **[Overridden method called during object construction]**: Reports calls to methods overridden in current class; dangerous in hierarchy.
*   **[Static field may not be initialized]**: Reports static fields that might be null after class init.
*   **[Static field used before initialization]**: Reports static fields used before assignment.
*   **[Unsafe lazy initialization of 'static' field]**: Reports lazy init of statics without synchronization; thread-unsafe.

## Inheritance Issues
*   **[Abstract class extends concrete class]**: Reports abstract classes extending concrete classes; suggests composition or interfaces to avoid fragility.
*   **[Abstract class which has no concrete subclass]**: Reports abstract classes that are never implemented; suggests removal or making concrete.
*   **[Abstract class without 'abstract' methods]**: Reports abstract classes with no abstract methods; suggests making concrete or checking design.
*   **[Abstract method overrides abstract method]**: Reports redundant abstract declarations that override another abstract method.
*   **[Abstract method overrides concrete method]**: Reports abstract methods overriding concrete ones; usually a design flaw.
*   **[Abstract method with missing implementations]**: Reports abstract methods not implemented in all subclasses (early detection).
*   **[Class explicitly extends a 'Collection' class]**: Reports classes extending `ArrayList` or `HashMap`; suggests delegation.
*   **[Class extends annotation interface]**: Reports classes extending `@interface`, which is invalid.
*   **[Class extends utility class]**: Reports extending utility classes; utility classes should be `final` with private constructors.
*   **[Final declaration can't be overridden at runtime]**: Reports `final` classes/methods that block frameworks (Spring, Hibernate) from creating proxies.
*   **[Interface which has no concrete subclass]**: Reports interfaces with no implementations; suggests removal.
*   **[Method does not call super method]**: Reports overrides of methods (like `clone()`) that fail to call `super`, breaking contracts.
*   **[Method is identical to its super method]**: Reports redundant overrides that explicitly delegates to `super`.
*   **[Missing '@Override' annotation]**: Reports missing `@Override` annotation; critical for detecting signature mismatches during refactoring.
*   **[Non-varargs method overrides varargs method]**: Reports overriding varargs with array parameters; confusing.
*   **[Parameter type prevents overriding]**: Reports parameter type mismatches (often package-private) that silently prevent overriding.
*   **[Public constructor in abstract class]**: Reports `public` constructors in `abstract` classes; suggests `protected`.
*   **[Redundant interface declaration]**: Reports explicit implementation of interfaces already implemented by superclasses.
*   **[Static inheritance]**: Reports implementing interfaces solely for constants; suggests static imports instead.
*   **[Type parameter extends 'final' class]**: Reports generics bounds like `T extends String`; redundant as `String` gives no extensibility.

## Internationalization Issues
*   **['SimpleDateFormat' without locale]**: Reports usages of date formatters without locale; can cause unexpected parsing/formatting in different regions.
*   **[Absolute alignment in AWT/Swing code]**: Reports absolute positioning; breaks layout on different screen sizes/locales.
*   **[Call to 'Date.toString()']**: Reports explicit `Date.toString()`; usually formatted date is preferred.
*   **[Call to 'Number.toString()']**: Reports `Number.toString()`; formatting numbers is usually locale-dependent.
*   **[Call to 'String.toUpperCase()' or 'toLowerCase()' without locale]**: Reports case conversion without locale; risky (e.g., Turkish 'I').
*   **[Call to 'Time.toString()']**: Reports `Time.toString()`; formatting logic should be explicit.
*   **[Call to suspicious 'String' method]**: Reports `equals()`/`compareTo()` on Strings that might be locale-sensitive.
*   **[Character comparison]**: Reports comparing chars (`c < 'a'`); may be incorrect for some alphabets.
*   **[Duplicate string literal]**: Reports reused string literals; suggests constants (i18n preparation).
*   **[Hardcoded strings]**: Reports string literals intended for UI; suggests resource bundles.
*   **[Implicit platform default charset]**: Reports methods verifying charset (e.g. `String.getBytes()`); suggests `StandardCharsets.UTF_8`.
*   **[Incorrect string capitalization]**: Reports strings not following capitalization guidelines (Title Case, etc.).
*   **[Magic character]**: Reports unnamed character literals; suggests constants.
*   **[Non-Basic Latin character]**: Reports special characters in source code; suggests Unicode escapes or ASCII.
*   **[String concatenation]**: Reports string concatenation in i18n contexts; suggests `MessageFormat`.
*   **[Unnecessary Unicode escape sequence]**: Reports Unicode escapes for ASCII characters; reads better as raw chars.
*   **[Use of 'StringTokenizer']**: Reports `StringTokenizer`; legacy class, use `split()` or `Pattern`.

## JUnit Issues
*   **[Test annotation without '@Retention(RUNTIME)' annotation]**: Reports meta-annotations missing `RUNTIME` retention; JUnit 5 won't see them.

## Java Language Level Migration Aids
*   **['compare()' method can be used to compare numbers]**: Reports verbose comparisons; suggests `Integer.compare()`.
*   **['if' can be replaced with 'switch']**: Reports `if-else` chains; suggests `switch`.
*   **[Enumeration can be iteration]**: Reports `Enumeration`; suggests `Iterator` or `for-each` loop.

## JavaBeans Issues
*   **[Class without constructor]**: Reports classes without an explicit constructor; suggests creating one (even simple).
*   **[Class without no-arg constructor]**: Reports missing no-arg constructor; required for JavaBeans, serialization, and many frameworks.
*   **[Field has setter but no getter]**: Reports write-only properties, which are often design flaws.
*   **[Property value set to itself]**: Reports `this.x = x` where `x` is the field itself (missing `this` or param); redundant.
*   **[Suspicious getter/setter]**: Reports accessors accessing fields not matching the method name (e.g., `getFoo()` accessing `bar`).

## Javadoc Issues
*   **['<code>...</code>' can be replaced with '{@code ...}']**: Reports HTML `<code>` tags; suggests `{@code}` for better formatting/validation.
*   **['package-info.java' without 'package' statement]**: Reports `package-info.java` missing the package declaration.
*   **['package.html' may be converted to 'package-info.java']**: Reports legacy `package.html`; suggests standard `package-info.java`.
*   **[Blank line should be replaced with <p> to break lines]**: Reports blank lines in Javadoc; suggests `<p>` for correct HTML rendering.
*   **[Comment replaceable with Javadoc]**: Reports `//` or `/*` comments on API elements; suggests `/** ... */`.
*   **[Dangling Javadoc comment]**: Reports Javadoc not attached to any declaration.
*   **[Declaration has problems in Javadoc references]**: Reports unresolved links/params in Javadoc.
*   **[HTML problems in Javadoc (DocLint)]**: Reports invalid HTML in Javadoc (e.g., unclosed tags).
*   **[Javadoc declaration problems]**: Reports invalid tags, duplicate param descriptions, etc.
*   **[Link specified as plain text]**: Reports raw URLs; suggests `{@link}` or `<a>`.
*   **[Mismatch between Javadoc and code]**: Reports descriptions contradicting checks (e.g., `@param x (null ok)` but annotated `@NotNull`).
*   **[Missing '@Deprecated' annotation]**: Reports Javadoc `@deprecated` without the annotation `@Deprecated`.
*   **[Missing 'package-info.java']**: Reports packages missing documentation files.
*   **[Missing Javadoc]**: Reports public API without Javadoc; suggests adding documentation.
*   **[Unnecessary '{@inheritDoc}' Javadoc comment]**: Reports Javadoc containing only `{@inheritDoc}`; usually redundant as it's default behavior.
*   **[Unnecessary Javadoc link]**: Reports self-referential links (linking to the method itself).

## Logging Issues
*   **['public' method without logging]**: Reports public methods without logging statements (if policy requires strict tracing).
*   **[Class with multiple loggers]**: Reports classes with >1 logger; suggests consolidation.
*   **[Class without logger]**: Reports classes missing a logger (if policy requires).
*   **[Logger initialized with foreign class]**: Reports logger init with wrong class (`Logger.getLogger(OtherClass.class)`).
*   **[Non-constant logger]**: Reports non-static/non-final loggers; suggests `private static final`.
*   **[Non-constant string concatenation as argument to logging call]**: Reports string concat in log calls; suggests parameterized logging (`log.info("{}", val)`) for performance.

## Lombok Issues
*   **[@Qualifier not copyable by Lombok]**: Reports Spring `@Qualifier` on fields not copied to Lombok constructors; suggests `lombok.copyableAnnotations`.
*   **[Deprecated Lombok annotations]**: Reports legacy annotations (e.g. `experimental`); suggests stable versions.
*   **[Lombok annotations]**: General check for Lombok usage issues/configuration.
*   **[Lombok flag usages]**: Checks usage against `lombok.config`.
*   **[Using static import for Lombok-generated methods]**: Reports static imports of Lombok methods, which can confuse IDEs/compilers.

## Method Metrics
*   **[Constructor with too many parameters]**: Reports constructors with huge parameter lists; suggests Builder pattern.
*   **[Method with more than three negations]**: Reports methods with confusing boolean logic (`!a && !b`); suggests simplification.
*   **[Method with multiple loops]**: Reports methods with multiple loops; suggests splitting.
*   **[Method with multiple return points]**: Reports methods with too many returns; suggests simplifying control flow.
*   **[Method with too many exceptions declared]**: Reports methods declaring excessive checked exceptions.
*   **[Method with too many parameters]**: Reports methods with wide signatures; suggests parameter objects.
*   **[Overly complex method]**: Reports high cyclomatic complexity; suggests refactoring/splitting.
*   **[Overly coupled method]**: Reports methods dependent on too many other classes.
*   **[Overly long lambda expression]**: Reports huge lambdas; suggests extracting to methods.
*   **[Overly long method]**: Reports huge methods (LOC); suggests splitting.
*   **[Overly nested method]**: Reports deep nesting; suggests guard clauses or extraction.

## Modularization Issues
*   **[Class independent of its module]**: Reports classes not used by/using their own module; suggests moving.
*   **[Class only used from one other module]**: Reports classes tightly coupled to another module; suggests moving to the consumer module.
*   **[Inconsistent language level settings]**: Reports modules depending on modules with higher language levels.
*   **[Module with too few classes]**: Reports tiny modules (granularity overhead).
*   **[Module with too many classes]**: Reports huge modules (monoliths).

## Memory Issues
*   **['StringBuilder' field]**: Reports `StringBuilder`/`StringBuffer` fields; growing buffers in long-lived objects can cause leaks/high consumption.
*   **[Anonymous class may be a named 'static' inner class]**: Reports anonymous classes that don't capture state; suggests named static inner class to save memory.
*   **[Call to 'System.gc()' or 'Runtime.gc()']**: Reports explicit GC calls; let the JVM handle memory.
*   **[Inner class may be 'static']**: Reports inner classes not using outer instance; suggests `static` to avoid holding outer reference.
*   **[Return of instance of anonymous, local or inner class]**: Reports returning non-static inner classes; risks retaining outer instance.
*   **[Static collection]**: Reports mutable static collections; likely memory leak source.
*   **[Unnecessary zero length array usage]**: Reports `new T[0]`; suggests using a constant (e.g. `Collections.emptyList()` or shared array).
*   **[Zero-length array allocation]**: Reports explicit `new T[0]`; suggests using constants to reduce garbage.

## Naming Conventions
*   **[Field naming convention]**: Reports fields violating naming rules (e.g. `s_name`); suggests camelCase.
*   **[Java module name violates convention]**: Reports module names ending in digits (versioning) which is discouraged.
*   **[Lambda parameter naming convention]**: Reports lambda params not following rules (e.g. too short/long).
*   **[Local variable naming convention]**: Reports local variables violating expectations.
*   **[Method parameter naming convention]**: Reports method parameters violating expectations.
*   **[Non-constant field with upper-case name]**: Reports non-static/non-final fields in `UPPER_CASE`; suggests camelCase.
*   **[Package naming convention]**: Reports packages with uppercase or weird chars; suggests lowercase.
*   **[Parameter name differs from parameter in overridden or overloaded method]**: Reports inconsistent param names in overrides.
*   **[Questionable name]**: Reports confusing names (e.g., `foo`, `bar`).
*   **[Standard variable names]**: Reports standard names (`i`, `s`) used for wrong types.
*   **[Use of '$' in identifier]**: Reports `$` in names; suggests removing (reserved for inner classes).

## Packaging Issues
*   **[Class independent of its package]**: Reports classes not using package-private members; suggests moving.
*   **[Class only used from one other package]**: Reports classes used only by one external package; suggests moving there.
*   **[Exception package]**: Reports packages containing *only* exceptions; usually an anti-pattern (group by feature).
*   **[Package with classes in multiple modules]**: Reports "split packages" (same package in different modules); breaks modularity.
*   **[Package with disjoint dependency graph]**: Reports packages performing multiple unrelated roles; suggests splitting.
*   **[Package with too few classes]**: Reports tiny packages.
*   **[Package with too many classes]**: Reports huge packages.

## Numeric Issues
*   **['char' expression used in arithmetic context]**: Reports arithmetic with chars (`'a' + 5`); often unintentional.
*   **['equals()' called on 'BigDecimal']**: Reports `BigDecimal.equals()` (sensitive to scale); suggests `compareTo() == 0`.
*   **['long' literal ending with 'l' instead of 'L']**: Reports `1l`; confusing with `11`; suggests `1L`.
*   **[Call to 'BigDecimal' method without a rounding mode argument]**: Reports division without rounding; throws `ArithmeticException` on non-terminating decimals.
*   **[Comparison of 'short' and 'char' values]**: Reports implicit signed/unsigned casting issues.
*   **[Comparison to 'Double.NaN' or 'Float.NaN']**: Reports `x == Double.NaN` (always false); suggests `Use Double.isNaN(x)`.
*   **[Confusing floating-point literal]**: Reports `1.` or `.5`; suggests `1.0` or `0.5` for readability.
*   **[Constant call to 'Math']**: Reports math calls with constants; suggests pre-calculating.
*   **[Division by zero]**: Reports obvious division/remainder by zero.
*   **[Floating-point equality comparison]**: Reports `d1 == d2`; imprecise; suggests using epsilon.
*   **[Implicit numeric conversion]**: Reports usages of implicit narrowing/widening that might lose precision.
*   **[Integer division in floating-point context]**: Reports `double d = 1 / 2;` (result 0.0); suggests `1.0 / 2`.
*   **[Negative int hexadecimal constant in long context]**: Reports valid but confusing sign extension; suggests `L` suffix or explicit cast.
*   **[Non-reproducible call to 'Math']**: Reports `Math` methods that vary by platform (e.g. `tan`); suggests `StrictMath`.
*   **[Number constructor call with primitive argument]**: Reports `new Integer(1)`; suggests `Integer.valueOf(1)` (cached).
*   **[Numeric literal can use underscore separators]**: Reports long numbers; suggests `1_000_000` for readability.
*   **[Numeric overflow]**: Reports constants causing overflow (`Integer.MAX_VALUE + 1`).
*   **[Octal and decimal integers in same array]**: Reports mix of `010` and `10`; highly confusing.
*   **[Octal integer]**: Reports usages of octal literals (`0123`); often typo for decimal.
*   **[Overly complex arithmetic expression]**: Reports deeply nested formulas; suggests splitting/refactoring.
*   **[Pointless arithmetic expression]**: Reports `x + 0` or `x * 1`.
*   **[Possibly lossy implicit cast in compound assignment]**: Reports `i += d` (casts `d` to int); losing data.
*   **[Suspicious oddness check]**: Reports `x % 2 == 1` (fails for negative numbers); suggests `x % 2 != 0`.
*   **[Suspicious underscore in number literal]**: Reports `1_00` (non-standard grouping).
*   **[Unary plus]**: Reports `+x`; usually redundant.
*   **[Underscores in numeric literal]**: Reports underscores if project style forbids them.
*   **[Unnecessary unary minus]**: Reports `- -x` or similar.
*   **[Unpredictable 'BigDecimal' constructor call]**: Reports `new BigDecimal(0.1)` (actually 0.100000...555); suggests `BigDecimal("0.1")`.

## Portability Issues
*   **[Call to 'Runtime.exec()']**: Reports usages of `Runtime.exec()`; usually non-portable.
*   **[Call to 'System.exit()' or related methods]**: Reports `System.exit()`; abrupt shutdown is bad for embedded/server apps.
*   **[Call to 'System.getenv()']**: Reports usages of `System.getenv()`; vars vary by OS.
*   **[Hardcoded file separator]**: Reports `/` or `\` in paths; suggests `File.separator`.
*   **[Hardcoded line separator]**: Reports `\n` or `\r`; suggests `%n` or `System.lineSeparator()`.
*   **[Native method]**: Reports `native` methods; limits portability.
*   **[Use of 'java.lang.ProcessBuilder' class]**: Reports `ProcessBuilder`; command syntax is OS-dependent.
*   **[Use of 'sun.*' classes]**: Reports usage of internal JDK classes; guaranteed to break.
*   **[Use of AWT peer class]**: Reports usage of AWT peers; implementation details.
*   **[Use of concrete JDBC driver class]**: Reports hardcoded JDBC drivers; suggests `DataSource` or `DriverManager`.

## Probable Bugs
*   **['assert' statement with side effects]**: Reports asserts changing state; enabled/disabled asserts shouldn't affect logic.
*   **['Comparable' implemented but 'equals()' not overridden]**: Reports missing `equals()`; consistency with `compareTo()` is recommended.
*   **['equal()' instead of 'equals()']**: Reports likely typo `equal()` vs `equals()`.
*   **['equals()' and 'hashCode()' not paired]**: Reports overriding one without the other; violates contract.
*   **['equals()' between objects of inconvertible types]**: Reports `x.equals(y)` where types fail equality check always.
*   **['equals()' called on array]**: Reports `array.equals()`; suggests `Arrays.equals()`.
*   **['equals()' called on classes which don't override it]**: Reports `equals` on `StringBuilder`/`AtomicInteger`; identity comparison is likely unintended.
*   **['equals()' called on itself]**: Reports `x.equals(x)`; redundant.
*   **['equals()' method that does not check the class of its parameter]**: Reports flawed `equals()` logic.
*   **['hashCode()' called on array]**: Reports `array.hashCode()`; suggests `Arrays.hashCode()`.
*   **['instanceof' with incompatible type]**: Reports impossible strict type checks.
*   **['Iterator.hasNext()' which calls 'next()']**: Reports `hasNext()` advancing the iterator; bug.
*   **['Iterator.next()' which can't throw 'NoSuchElementException']**: Reports incorrect iterator implementation.
*   **['Math.random()' cast to 'int']**: Reports `(int) Math.random()` which is always 0; bug.
*   **['ScheduledThreadPoolExecutor' with zero core threads]**: Reports bad config; executor won't run.
*   **['String.equals()' called with 'CharSequence' argument]**: Reports `str.equals(stringBuilder)`; likely false.
*   **['Throwable' not thrown]**: Reports `new Exception()` that is dropped; missing `throw`.
*   **[@SafeVarargs do not suppress potentially unsafe operations]**: Reports unsafe varargs despite annotation.
*   **[Array comparison using '==', instead of 'Arrays.equals()']**: Reports `arr1 == arr2`; usually wrong (identity vs content).
*   **[Call math rounding with 'int' argument]**: Reports redundant rounding on integers.
*   **[Call methods with unsupported 'java.time.temporal.ChronoUnit'...]**: Reports invalid time unit usage.
*   **[Call to 'toString()' on array]**: Reports `array.toString()` (prints memory address); suggests `Arrays.toString()`.
*   **[Call to default 'toString()']**: Reports `Object.toString()` output; usually uninformative.
*   **[Cast conflicts with 'instanceof']**: Reports illogical casts.
*   **[Cast to incompatible type]**: Reports `ClassCastException` hazards.
*   **[Cleaner captures object reference]**: Reports lambda passed to Cleaner capturing the object itself (prevents cleanup).
*   **[Collection added to itself]**: Reports `list.add(list)`; infinite recursion risk.
*   **[Confusing 'main()' method]**: Reports `main()` with wrong signature; won't run.
*   **[Confusing argument to varargs method]**: Reports ambiguous vararg calls.
*   **[Confusing primitive array argument to varargs method]**: Reports `foo(intArray)` vs `foo(Integer...)`.
*   **[Constant condition in 'assert' statement]**: Reports `assert true` or `assert false`; pointless.
*   **[Constant values]**: Reports useless checks (`if (true)`).
*   **[Contract issues]**: Reports `@Contract` violations.
*   **[Copy constructor misses field]**: Reports incomplete copy constructors.
*   **[Covariant 'equals()']**: Reports `equals(MyType)` instead of `equals(Object)`; overloading vs overriding error.
*   **[Duplicated delimiters in 'StringTokenizer']**: Reports `StringTokenizer(s, "AA")`; likely typo.
*   **[Expression is compared to itself]**: Reports `x == x`.
*   **[Inconsistent whitespace indentation in text block]**: Reports mixed tabs/spaces.
*   **[Incorrect 'DateTimeFormat' pattern]**: Reports bad patterns.
*   **[Incorrect 'MessageFormat' pattern]**: Reports bad patterns.
*   **[Infinite recursion]**: Reports methods calling themselves without exit.
*   **[Inner class referenced via subclass]**: Reports confusing scope access.
*   **[Instantiation of utility class]**: Reports `new MathUtils()`; utility classes should be static-only.
*   **[Invalid method reference used for 'Comparator']**: Reports broken comparators.
*   **[Iterable is used as vararg]**: Reports passing Iterable to vararg; treated as single object, not spread.
*   **[Loop executes zero or billions of times]**: Reports overflowing loops.
*   **[Magic constant]**: Reports non-constant magic values.
*   **[Malformed format string]**: Reports `printf` errors.
*   **[Meaningless record annotation]**: Reports invalid record annotations.
*   **[Mismatched case in 'String' operation]**: Reports `str.toUpperCase().equals("lower")`.
*   **[Mismatched query and update of 'StringBuilder']**: Reports write-only or read-only buffers.
*   **[Mismatched query and update of collection]**: Reports write-only or read-only collections.
*   **[Mismatched read and write of array]**: Reports write-only or read-only arrays.
*   **[New object is compared using '==']**: Reports `new Object() == new Object()`; always false.
*   **[Non-final field referenced in 'compareTo()']**: Reports inconsistent comparison logic.
*   **[Non-final field referenced in 'equals()']**: Reports inconsistent equality logic.
*   **[Non-final field referenced in 'hashCode()']**: Reports inconsistent hash codes (keys might get lost in Map).
*   **[Non-short-circuit boolean expression]**: Reports `&` instead of `&&`; usually typo.
*   **[Non-short-circuit operation consumes infinite stream]**: Reports infinite loop risk.
*   **[Nullability and data flow problems]**: Reports NPEs / redundant null checks.
*   **[Number comparison using '==', instead of 'equals()']**: Reports `num1 == num2` (objects); unsafe.
*   **[Object comparison using '==', instead of 'equals()']**: Reports object identity checks where content equality is expected.
*   **[Optional.get() is called without isPresent() check]**: Reports unsafe `Optional` usage; suggests `orElseThrow`.
*   **[Overwritten Map, Set, or array element]**: Reports `map.put(k, v1); map.put(k, v2);`; duplicate keys.
*   **[Redundant operation on empty container]**: Reports `emptyList.clear()`.
*   **[Reference checked for 'null' is not used inside 'if']**: Reports pointless null checks.
*   **[Reflective access to a source-only annotation]**: Reports reading annotations not available at runtime.
*   **[Result of method call ignored]**: Reports ignored returns (e.g. `file.delete()` result ignored).
*   **[Result of object allocation ignored]**: Reports `new Object();` doing nothing.
*   **[Return value is outside of declared range]**: Reports violations of `@Range` annotations.
*   **[Sorted collection with non-comparable elements]**: Reports `TreeSet<Object>`; throws `ClassCastException`.
*   **[Statement with empty body]**: Reports `if (cond);`; typo.
*   **[Static field referenced via subclass]**: Reports misleading static access.
*   **[Static method referenced via subclass]**: Reports misleading static calls.
*   **[String comparison using '==', instead of 'equals()']**: Reports `str1 == str2`.
*   **[String concatenation as argument to 'format()' call]**: Reports `String.format("..." + val)`; defeats purpose of format.
*   **[String concatenation as argument to 'MessageFormat.format()' call]**: Reports `MessageFormat.format("..." + val)`.
*   **[StringBuilder constructor call with 'char' argument]**: Reports `new StringBuilder('c')` (int capacity) vs `new StringBuilder("c")` (content); common bug.
*   **[Subtraction in 'compareTo()']**: Reports `return a - b;` (overflow risk); suggests `Integer.compare(a, b)`.
*   **[Suspicious 'Arrays' method call]**: Reports mismatching types in `Arrays` utils.
*   **[Suspicious 'Class.getClass()' call]**: Reports `clazz.getClass()`.
*   **[Suspicious 'Collection.toArray()' call]**: Reports invalid array types.
*   **[Suspicious 'Comparator.compare()' implementation]**: Reports incorrect comparison logic.
*   **[Suspicious 'InvocationHandler' implementation]**: Reports handlers breaking contracts.
*   **[Suspicious 'List.remove()' in loop]**: Reports `remove(int)` vs `remove(Object)` confusion.
*   **[Suspicious 'System.arraycopy()' call]**: Reports bad ranges/types.
*   **[Suspicious array cast]**: Reports invalid casts.
*   **[Suspicious byte value returned from 'InputStream.read()']**: Reports byte/int confusion (-1 check).
*   **[Suspicious collection method call]**: Reports `list.contains(wrongType)`.
*   **[Suspicious date format pattern]**: Reports typo in pattern.
*   **[Suspicious indentation after control statement without braces]**: Reports misleading indentation (Python-style bug).
*   **[Suspicious integer division assignment]**: Reports `double d = 1/2`.
*   **[Suspicious regex expression argument]**: Reports `replaceAll(".", "*")` (replaces everything); literal vs regex confusion.
*   **[Suspicious ternary operator in varargs method call]**: Reports ambiguity.
*   **[Suspicious usage of compare method]**: Reports `x.compareTo(y) == 1`; implementation dependent (should be `> 0`).
*   **[Suspicious variable/parameter name combination]**: Reports `setX(y)`.
*   **[Text label in 'switch' statement]**: Reports `case 1: ... default: ... label:` (often expected `case label:`).
*   **[Unreachable code]**: Reports dead code.
*   **[Unsafe call to 'Class.newInstance()']**: Reports deprecated/unsafe usage; suggests `Constructor.newInstance()`.
*   **[Unused assignment]**: Reports assignments overwritten before read.
*   **[Use of 'Properties' object as a 'Hashtable']**: Reports using `put()` instead of `setProperty()` (non-String keys).
*   **[Use of index 0 in JDBC ResultSet]**: Reports `get(0)`; JDBC is 1-indexed.
*   **[Use of Optional.ofNullable with null or non-null argument]**: Reports known non-nulls.
*   **[Use of shallow or 'Objects' methods with arrays]**: Reports shallow equality on arrays.
*   **[Whitespace may be missing in string concatenation]**: Reports `s + "string"` (missing space).
*   **[Write-only object]**: Reports dead stores.
*   **[Wrong package statement]**: Reports package mismatch with directory.

## Reflective Access
*   **[MethodHandle/VarHandle type mismatch]**: Reports handle creation where types don't match target.
*   **[Reflective access across modules issues]**: Reports Java 9+ module visibility violations in reflection.
*   **[Reflective access to non-existent or not visible class member]**: Reports `getMethod("missing")`.
*   **[Reflective invocation arguments mismatch]**: Reports `method.invoke(obj, wrongArgs)`.

## Resource Management
*   **['Channel' opened but not safely closed]**: Reports `Channel` leaks.
*   **[AutoCloseable used without 'try'-with-resources]**: Reports manual close; suggests `try (...)`.
*   **[Hibernate resource opened but not safely closed]**: Reports `Session` leaks.
*   **[I/O resource opened but not safely closed]**: Reports `InputStream`/`Reader` leaks.
*   **[JDBC resource opened but not safely closed]**: Reports `Connection`/`Statement` leaks.
*   **[JNDI resource opened but not safely closed]**: Reports `Context` leaks.
*   **[Socket opened but not safely closed]**: Reports `Socket` leaks.
*   **[Use of 'DriverManager' to get JDBC connection]**: Reports direct `DriverManager` usage; suggests `DataSource`.

## Security Issues
*   **['ClassLoader' instantiation]**: Reports `new ClassLoader()`; security risk.
*   **['public static' array field]**: Reports mutable static arrays; thread-safety/security risk (malicious code can modify slots).
*   **['public static' collection field]**: Reports mutable static collections; suggests `Collections.unmodifiableList`.
*   **[Access of system properties]**: Reports `System.getProperties()`; often restricted.
*   **[Call to 'Connection.prepare*()' with non-constant string]**: Reports SQL Injection risk.
*   **[Call to 'Runtime.exec()' with non-constant string]**: Reports Command Injection risk.
*   **[Call to 'Statement.execute()' with non-constant string]**: Reports SQL Injection risk.
*   **[Call to 'System.loadLibrary()' with non-constant string]**: Reports DLL Hijacking risk.
*   **[Call to 'System.setSecurityManager()']**: Reports tampering with security manager.
*   **[Cloneable class in secure context]**: Reports `Cloneable` which bypasses constructor checks.
*   **[Custom 'ClassLoader' is declared]**: Reports custom loaders; high risk.
*   **[Custom 'SecurityManager']**: Reports custom managers.
*   **[Design for extension]**: Reports overridable methods in secure classes.
*   **[Insecure random number generation]**: Reports `Math.random()`/`Random`; suggests `SecureRandom` for crypto.
*   **[Non-final 'clone()' in secure context]**: Reports overrideable clone.
*   **[Serializable class in secure context]**: Reports serialization; huge attack surface.

## Test Frameworks
*   **[Assertion is suppressed by 'catch']**: Reports asserts inside `catch` blocks that might be ignored.
*   **[Constant assert argument]**: Reports `assertTrue(true)`; pointless.
*   **[Message missing on assertion]**: Reports asserts without failure messages; hard to debug.
*   **[Misordered 'assertEquals()' arguments]**: Reports `assertEquals(actual, expected)`; confusing output.
*   **[Simplifiable assertion]**: Reports `assertTrue(a == b)`; suggests `assertEquals(a, b)`.

## Properties Issues
*   **[Invalid property key]**: Reports invalid keys passed to `@PropertyKey` methods.
*   **[Unsupported character]**: Reports characters not supported by ISO-8859-1 (Java 8-).

## Serialization Issues
*   **['@Serial' annotation can be used]**: Reports missing `@Serial` on serialization methods (Java 14+).
*   **['@Serial' annotation used on wrong member]**: Reports incorrect usage of `@Serial`.
*   **['Comparator' class not declared 'Serializable']**: Reports Comparators usually need to be serializable if strict.
*   **['Externalizable' class without 'public' no-arg constructor]**: Reports `Externalizable` classes violating contract.
*   **['readObject()' or 'writeObject()' not declared 'private']**: Reports visibility issues; serialization magic methods must be private.
*   **['readResolve()' or 'writeReplace()' not declared 'protected']**: Reports visibility issues; useful for inheritance.
*   **['record' contains ignored members]**: Reports fields in records that are ignored during serialization.
*   **['Serializable' object implicitly stores non-'Serializable' object]**: Reports anonymous classes/lambdas holding non-serializable refs.
*   **['serialPersistentFields' field not declared 'private static final ObjectStreamField[]']**: Reports signature mismatch.
*   **['serialVersionUID' field not declared 'private static final long']**: Reports signature mismatch.
*   **[Externalizable class with 'readObject()' or 'writeObject()']**: Reports redundant methods; `Externalizable` uses `readExternal`/`writeExternal`.
*   **[Instance field may not be initialized by 'readObject()']**: Reports fields left null after deserialization.
*   **[Non-serializable class with 'readObject()' or 'writeObject()']**: Reports serialization methods on non-serializable classes (useless).
*   **[Non-serializable class with 'serialVersionUID']**: Reports useless `serialVersionUID`.
*   **[Non-serializable field in a 'Serializable' class]**: Reports fields that will cause `NotSerializableException`.
*   **[Non-serializable object bound to 'HttpSession']**: Reports web session objects that fail clustering.
*   **[Non-serializable object passed to 'ObjectOutputStream']**: Reports runtime errors.
*   **[Serializable class in secure context]**: Reports serialization; huge attack surface.
*   **[Serializable class with unconstructable ancestor]**: Reports superclass missing no-arg constructor; deserialization will fail.
*   **[Serializable class without 'readObject()' and 'writeObject()']**: Reports insecure default serialization.
*   **[Serializable non-'static' inner class with non-Serializable outer class]**: Reports serialization failure risk.
*   **[Serializable non-static inner class without 'serialVersionUID']**: Reports missing UID.
*   **[Transient field in non-serializable class]**: Reports redundant `transient`.
*   **[Transient field is not initialized on deserialization]**: Reports logic errors; transient fields need manual init in `readObject`.

## Verbose or Redundant Code
*   **['StringBuilder' can be replaced with 'String']**: Reports `new StringBuilder("a").append("b").toString()` vs `"a" + "b"`.
*   **[Cast can be replaced with variable]**: Reports redundant casts if variable of that type exists.
*   **[Comparator method can be simplified]**: Reports complex comparator chains replaceable by simple `Comparator.comparing()`.
*   **[Concatenation with empty string]**: Reports `"" + x`.
*   **[Condition is covered by further condition]**: Reports redundant logic checks.
*   **[Copy of existing static method body]**: Reports code duplication of standard library methods.
*   **[Duplicate branches in 'switch']**: Reports copy-pasted switch cases.
*   **[Excessive lambda usage]**: Reports lambdas where method references or direct values work.
*   **[Excessive range check]**: Reports `x > 0 && x > 5` (redundant).
*   **[Explicit array filling]**: Reports loops replaceable by `Arrays.fill()`.
*   **[Lombok @Getter/@Setter may be used]**: Reports vanilla getters/setters replaceable by Lombok.
*   **[Manual min/max calculation]**: Reports `if (a < b) a` vs `Math.min(a, b)`.
*   **[Mapping call before count()]**: Reports `stream.map(...).count()`; mapping doesn't change count.
*   **[Multiple occurrences of the same expression]**: Reports repeated calculations; suggests variable extraction.
*   **[Non-strict inequality '>=' or '<=' can be replaced with '==']**: Reports logic simplification.
*   **[Null-check method is called with obviously non-null argument]**: Reports redundant `requireNonNull(new Object())`.
*   **[Only one element is used]**: Reports `list.get(0)` on fresh list; suggests scalar.
*   **[Optional call chain can be simplified]**: Reports complex Optional logic.
*   **[Redundant 'Collection' operation]**: Reports usage like `c.containsAll(Collections.singleton(x))`.
*   **[Redundant 'compare()' method call]**: Reports redundant comparisons.
*   **[Redundant 'File' instance creation]**: Reports `new FileReader(new File(...))` vs `new FileReader(...)`.
*   **[Redundant 'isInstance()' or 'cast()' call]**: Reports pointless reflection.
*   **[Redundant 'String' operation]**: Reports `str.toString()` or `new String()`.
*   **[Redundant array creation]**: Reports `new Object[] { ... }` in varargs calls.
*   **[Redundant array length check]**: Reports checks covered by loop bounds.
*   **[Redundant embedded expression in string template]**: Reports useless expressions in Java 21 templates.
*   **[Redundant escape in regex replacement string]**: Reports `\$` where `$` suffices.
*   **[Redundant operation on 'java.time' object]**: Reports unnecessary time conversions.
*   **[Redundant step in 'Stream' or 'Optional' call chain]**: Reports `filter(x -> true)` or `map(x -> x)`.
*   **[Redundant type arguments]**: Reports explicit generics where inference works.
*   **[Redundant type cast]**: Reports casts to same or super type.
*   **[Redundant usage of unmodifiable collection wrappers]**: Reports wrapping already immutable collections.
*   **[Replacement operation has no effect]**: Reports `str.replace("a", "a")`.
*   **[Simplifiable collector]**: Reports `collect(toList())` vs `toList()` (Java 16+).
*   **[Stream API call chain can be simplified]**: Reports various stream simplifications.
*   **[Too weak variable type leads to unnecessary cast]**: Reports variable type should be strengthened.
*   **[Unnecessarily escaped character]**: Reports `\a` (not special).
*   **[Unnecessary 'break'/'continue'/'return' statement]**: Reports control flow noise.
*   **[Unnecessary 'default' for enum 'switch' statement]**: Reports dead default if all enums covered.
*   **[Unnecessary label on 'break'/'continue' statement]**: Reports useless labels.
*   **[Unreachable catch section]**: Reports catches for exceptions never thrown.
*   **[Volatile array field]**: Reports volatile arrays (reference volatile, elements not).

## Visibility Issues
*   **['public' constructor in non-public class]**: Reports misleading visibility.
*   **[Access to inherited field looks like access to element from surrounding code]**: Reports ambiguity.
*   **[Anonymous class variable hides variable in containing method]**: Reports shadowing.
*   **[Call to inherited method looks like call to local method]**: Reports ambiguity.
*   **[Class is exposed outside of its visibility scope]**: Reports public method returning package-private type.
*   **[Empty 'module-info.java' file]**: Reports useless module descriptor.
*   **[Inner class field hides outer class field]**: Reports shadowing.
*   **[Lambda parameter hides field]**: Reports shadowing.
*   **[Local variable hides field]**: Reports shadowing.
*   **[Method overrides inaccessible method of superclass]**: Reports confusion (not true override).
*   **[Method tries to override 'static' method of superclass]**: Reports static method hiding (not overriding).
*   **[Module exports/opens package to itself]**: Reports useless module config.
*   **[Parameter hides field]**: Reports shadowing.
*   **[Pattern variable hides field]**: Reports shadowing in `instanceof`.
*   **[Possibly unintended overload of method from superclass]**: Reports overloading vs overriding confusion.
*   **[Subclass field hides superclass field]**: Reports shadowing.
*   **[Type parameter hides visible type]**: Reports generics shadowing.
*   **[Usage of service not declared in 'module-info']**: Reports Java 9 service loading definition mismatch.

## toString() Issues
*   **[Class does not override 'toString()' method]**: Reports classes relying on `Object.toString()` (identity).
*   **[Field not used in 'toString()' method]**: Reports incomplete `toString()` implementations.

## TestNG Issues
*   **[Data provider problems]**: Reports missing key references.
*   **[Duplicated data provider names]**: Reports naming collisions.
*   **[Expected exception never thrown in test method body]**: Reports tests passing despite missing exception.
*   **[Illegal method name passed to 'dependsOnMethods']**: Reports invalid dependencies.
*   **[Invalid data provider return type]**: Reports providers not returning `Object[][]` or `Iterator<Object[]>`.
*   **[JUnit Test can be converted to TestNG]**: Reports migration opportunity.
*   **[Old TestNG annotation @Configuration is used]**: Reports deprecated annotations.
*   **[TestNG Javadoc can be converted to annotations]**: Reports legacy Javadoc tags.
*   **[Undeclared test]**: Reports tests missing from `testng.xml`.
*   **[Undefined group name]**: Reports typos in group filters.

## Threading Issues
*   **['AtomicFieldUpdater' field not declared 'static final']**: Reports improper field updater usage.
*   **['await()' not called in loop]**: Reports spurious wakeups vulnerability.
*   **['await()' without corresponding 'signal()']**: Reports deadlock risk.
*   **['notify()' or 'notifyAll()' called on 'java.util.concurrent.locks.Condition' object]**: Reports mix-up between Monitors and Locks.
*   **['notify()' or 'notifyAll()' without corresponding state change]**: Reports pointless signaling.
*   **['notify()' without corresponding 'wait()']**: Reports signal logic errors.
*   **['signal()' without corresponding 'await()']**: Reports signal logic errors.
*   **['synchronized' method]**: Reports synchronized methods (monitor on `this`); suggests internal lock object.
*   **['ThreadLocal' field not declared 'static final']**: Reports misuse often leading to memory leaks.
*   **['ThreadLocal.set()' with null as an argument]**: Reports redundant `set(null)`; `remove()` is better.
*   **['ThreadLocalRandom' instance might be shared]**: Reports sharing `ThreadLocalRandom`; defeats the purpose.
*   **['wait()' called on 'java.util.concurrent.locks.Condition' object]**: Reports API confusion.
*   **['wait()' not called in loop]**: Reports spurious wakeups vulnerability.
*   **['wait()' or 'await()' without timeout]**: Reports deadlock risk.
*   **['wait()' or 'notify()' is not in synchronized context]**: Reports `IllegalMonitorStateException`.
*   **['wait()' while holding two locks]**: Reports deadlock risk.
*   **['wait()' without corresponding 'notify()']**: Reports deadlock risk.
*   **['while' loop spins on field]**: Reports CPU burning wait; suggests wait/notify or latches.
*   **[Access to 'static' field locked on instance data]**: Reports ineffective locking.
*   **[Busy wait]**: Reports `sleep()` in loop; suggests better concurrency primitives.
*   **[Call to 'notify()' instead of 'notifyAll()']**: Reports lost wakeups risk; `notifyAll` is safer.
*   **[Call to 'signal()' instead of 'signalAll()']**: Reports lost wakeups risk.
*   **[Call to 'System.runFinalizersOnExit()']**: Reports deprecated/unsafe method.
*   **[Call to 'Thread.setPriority()']**: Reports unpredictable behavior; don't rely on priorities.
*   **[Call to 'Thread.sleep()' while synchronized]**: Reports blocking a lock for long time; scalability killer.
*   **[Call to 'Thread.start()' during object construction]**: Reports `this` escape.
*   **[Call to 'Thread.stop()', 'suspend()' or 'resume()']**: Reports deprecated/unsafe methods.
*   **[Call to 'Thread.yield()']**: Reports unpredictable behavior.
*   **[Call to a 'native' method while locked]**: Reports blocking risks.
*   **[Class directly extends 'Thread']**: Reports inheritance abuse; implement `Runnable`.
*   **[Double-checked locking]**: Reports broken DCL (unless `volatile`).
*   **[Empty 'synchronized' statement]**: Reports useless code.
*   **[Field accessed in both 'synchronized' and unsynchronized contexts]**: Reports atomicity violations.
*   **[Inconsistent 'AtomicFieldUpdater' declaration]**: Reports setup errors.
*   **[Instantiating a 'Thread' with default 'run()' method]**: Reports useless thread.
*   **[Lock acquired but not safely unlocked]**: Reports missing `finally` block unlock.
*   **[Method with single 'synchronized' block can be replaced with 'synchronized' method]**: Reports style preference.
*   **[Nested 'synchronized' statement]**: Reports potential deadlock/complexity.
*   **[Non-atomic operation on 'volatile' field]**: Reports `volatile i++` (not atomic).
*   **[Non-private field accessed in 'synchronized' context]**: Reports leaky abstraction.
*   **[Non-thread-safe 'static' field access]**: Reports concurrent modification bugs.
*   **[Static initializer references subclass]**: Reports initialization deadlocks/cycles.
*   **[Synchronization on 'getClass()']**: Reports locking on class literal of subclass; risky.
*   **[Synchronization on 'static' field]**: Reports global lock contention risks.
*   **[Synchronization on 'this']**: Reports locking on public object; client can DDOS with external lock.
*   **[Synchronization on a 'Lock' object]**: Reports locking on lock object itself (mixup).
*   **[Synchronization on a non-final field]**: Reports locking on mutable reference; lock identity changes.
*   **[Synchronization on an object initialized with a literal]**: Reports locking on interned strings; global deadlock risk.
*   **[Synchronization on local variable or method parameter]**: Reports useless local lock.
*   **[Unconditional 'wait()' call]**: Reports logic error.
*   **[Unsynchronized method overrides 'synchronized' method]**: Reports atomicity loss.
*   **[Volatile array field]**: Reports `volatile` ref to array (elements not volatile).

## Performance Issues
*   **['Collection.toArray()' call style]**: Reports `list.toArray(new T[0])` vs pre-sized; optimized style depends on JVM version.
*   **['equals()' call can be replaced with '==']**: Reports `equals()` on types (like Enums) where `==` is safe and faster.
*   **['InputStream' and 'OutputStream' can be constructed using 'Files' methods]**: Reports `new FileInputStream()`; suggests `Files.newInputStream()` (NIO, better caching).
*   **['List.remove()' called in loop]**: Reports `remove()` in loop (O(n^2)); suggests `removeAll()` or `subList().clear()`.
*   **['Map' can be replaced with 'EnumMap']**: Reports `HashMap<Enum, V>`; suggests `EnumMap` (faster, compact).
*   **['Set' can be replaced with 'EnumSet']**: Reports `HashSet<Enum>`; suggests `EnumSet` (bit vector, very fast).
*   **['String.equals()' can be replaced with 'String.isEmpty()']**: Reports `"".equals(str)`; suggests `str.isEmpty()` (faster check).
*   **['StringBuilder' without initial capacity]**: Reports `new StringBuilder()` in loops; suggests sizing.
*   **[Auto-boxing]**: Reports hidden object creation (int -> Integer); expensive in tight loops.
*   **[Auto-unboxing]**: Reports unwrapping (Integer -> int); risk of NPE and overhead.
*   **[Boolean constructor call]**: Reports `new Boolean(b)`; memory waste; suggests `Boolean.valueOf(b)`.
*   **[Boxing of already boxed value]**: Reports redundant packaging.
*   **[Bulk 'Files.readAttributes()' call can be used]**: Reports multiple FS stats calls; suggests single bulk read.
*   **[Bulk operation can be used instead of iteration]**: Reports `for` loop adding to collection; suggests `addAll`.
*   **[Call to 'Arrays.asList()' with too few arguments]**: Reports `Arrays.asList(x)`; suggests `Collections.singletonList(x)`.
*   **[Call to 'list.containsAll(collection)' may have poor performance]**: Reports O(n*m) complexity; suggests converting to Set (O(n)).
*   **[Call to 'set.removeAll(list)' may work slowly]**: Reports set removal using list; suggest switching argument types if possible.
*   **[Call to simple getter/setter from within class]**: Reports method overhead; suggests direct field access (micro-optimization).
*   **[Collection without initial capacity]**: Reports collections in loops without size hint.
*   **[Dynamic regular expression can be replaced by compiled 'Pattern']**: Reports `str.matches(regex)`; suggests `Pattern.compile()` constant.
*   **[Early loop exit in 'if' condition]**: Reports optimization opportunities.
*   **[Explicit argument can be lambda]**: Reports anonymous classes replaceable by lambdas (invokedynamic is usually faster/lighter).
*   **[Field can be made 'static']**: Reports instance fields not capturing instance state; suggests static (memory savings).
*   **[Inefficient Stream API call chains ending with count()]**: Reports `stream().filter().count()`; some cases optimized, others not.
*   **[Instance initializer can be made 'static']**: Reports instance blocks `{}` not using instance state.
*   **[Instantiating object to get 'Class' object]**: Reports `new Foo().getClass()`; suggests `Foo.class`.
*   **[Iteration over 'keySet()' can be optimized]**: Reports iterating keys to get values; suggests `entrySet()`.
*   **[Manual array copy]**: Reports loop copy; suggests `System.arraycopy()` (native/intrinsic).
*   **[Method can be made 'static']**: Reports methods not touching instance state (`this`); suggests static (call speed/clarity).
*   **[Non-constant 'String' can be replaced with 'StringBuilder']**: Reports `str += val` in loops; catastrophic O(n^2) performance.
*   **[Object allocation in loop]**: Reports allocations inside hot loops; pressure on GC.
*   **[Redundant 'Collection.addAll()' call]**: Reports creation then addAll; suggests constructor usage.
*   **[Single character string argument in 'String.indexOf()' call]**: Reports `indexOf("c")`; suggests `indexOf('c')` (faster).
*   **[String concatenation]**: Reports `+` operator in loops or args; implies `StringBuilder` hidden creation.
*   **[Tail recursion]**: Reports methods tail-calling; Java doesn't optimize stack, so usually loop is better.
*   **[Unnecessary temporary object in conversion from/to 'String']**: Reports waste during conversions.
*   **[Wrapper type may be primitive]**: Reports `Integer i = 0`; suggests `int`.

## General Java Best Practices (not covered in JetBrains Inspectopedia)

### Readability & Naming
*   **Clarity**: Ensure code is easy to understand.
*   **Classes**: Use **PascalCase**. Must be nouns (e.g., `OrderService`).
*   **Methods**: Use **camelCase**. Must be verbs indicating action (e.g., `calculateTotal`).
*   **Variables**: Use **camelCase**. Avoid single letters unless in short loops.
*   **Constants**: Use **SCREAMING_SNAKE_CASE** (e.g., `MAX_RETRY_COUNT`).
*   **No Magic Values**: Avoid hardcoded numbers or strings. Use constants or enums. Skip checks on enum classes and test packages

### formatting & Style
*   **Consistency**: Maintain consistent indentation and line lengths.
*   **Tools**: Enforce standards automatically using static analysis tools like **SonarQube** or **Checkstyle**.
*   **Imports**: Remove all **unused imports**. Auto-organize imports.

### Error Prevention & Performance
*   **Null Safety**: Avoid `NullPointerException`. Use **`Optional`** or perform explicit null checks. **Exception**: This rule does not apply to **Enum** classes.
*   **Boolean Checks**: When checking non-primitive `Boolean` values, use `BooleanUtils.isTrue(value)` instead of direct access to avoid NPEs (e.g., `if(BooleanUtils.isTrue(applicant.getIsActive()))`).
*   **String Manipulation**: Use `StringBuilder` for string concatenation inside loops to optimize performance.
*   **Duplication (DRY)**: Refactor repetitive code into reusable methods or utility classes.

### Modularity & Design Principles
*   **Single Responsibility (SRP)**: Each class/method should have exactly one purpose.
*   **Composition over Inheritance**: Prefer composition to reduce coupling.
*   **Interfaces**: Code to interfaces (e.g., `List` instead of `ArrayList`), not implementations.

## Spring Boot Architecture & Configuration (not covered in JetBrains Inspectopedia)

### Project Structure
*   **Main Class**: explicit location in the root package to ensure correct component scanning (`@SpringBootApplication`).
*   **Layered Architecture**: Strict separation of concerns:
    *   **Controller**: Handles HTTP requests/responses.
    *   **Service**: Contains all business logic.
    *   **Repository**: Manages data access.

### Configuration Management
*   **Externalization**: Move environment-specific configs (DB creds, API keys) to `application.properties`, `application.yml`, or secure vaults.
*   **Security**: **NEVER** hardcode sensitive data (passwords, PII) in source code.
*   **Profiles**: Use `@Profile` annotations to define environment-specific beans (e.g., dev vs. prod).

## REST API Best Practices (not covered in JetBrains Inspectopedia)

*   **Naming**: Use consistent, plural resource names (e.g., `/api/v1/customers/{id}`).
*   **DTOs**: **Always** use Data Transfer Objects. **Never** expose JPA entities directly to clients.
*   **Validation**: Validate inputs using `@Valid` and Bean Validation annotations (`@NotNull`, `@Email`).
*   **Status Codes**: Return appropriate HTTP status codes:
    *   `200 OK`: Success.
    *   `201 Created`: Resource successfully created.
    *   `400 Bad Request`: Validation errors.
    *   `404 Not Found`: Resource does not exist.
    *   `500 Internal Server Error`: Generic handling.

## Service Layer & Data Access (JPA) (not covered in JetBrains Inspectopedia)

*   **Placement**: Business logic belongs in the **Service** layer, not Controllers or Repositories.
*   **Transactions**:
    *   Use `@Transactional` on service methods modifying data.
    *   Use `@Transactional(readOnly = true)` for read operations to optimize performance.
*   **Performance**:
    *   **Lazy Loading**: Ensure associations use `FetchType.LAZY` defaults to avoid N+1 query problems.
    *   **Pagination**: Use `Pageable` for fetching large datasets.
*   **Injection**: Use **Constructor Injection** (`final` fields) instead of `@Autowired` on fields.
*   **Audit Fields**: Fields like `created_at` and `updated_at` should **not** exist directly in classes annotated with `@Entity`.

## Error Handling, Logging & Security (not covered in JetBrains Inspectopedia)

*   **Global Handling**: Use `@ControllerAdvice` for centralized exception handling to ensure consistent JSON error responses.
*   **Logging**:
    *   Use **SLF4J** with Logback. Avoid `System.out.println()`.
    *   **Mandatory Service Logging**: Service layer methods should have **at least one** log message.
    *   Do **not** log sensitive information (passwords, PII).
*   **Security**:
    *   Verify **Spring Security** configuration.
    *   Sanitize inputs to prevent **SQL Injection** and **XSS**.