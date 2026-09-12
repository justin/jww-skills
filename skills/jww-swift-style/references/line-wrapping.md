# Swift Line Wrapping

Use these examples when nearby code does not settle a wrapping decision.
Repository instructions, formatter settings, and surrounding code take
precedence. The snippets illustrate layout, not application behavior; their
supporting types and functions are omitted.

These are starter examples for Justin to review and edit. Until that review,
treat them as illustrative options rather than settled personal conventions.

## Calls That Fit on One Line

Keep a short call on one line when it fits the configured limit and matches
nearby code. Multiple arguments alone do not require wrapping.

```swift
let request = makeRequest(query: query, limit: 20)
```

## Calls That Need Wrapping

One argument per line makes a long call easy to scan. Indent arguments one
level and align the closing parenthesis with the start of the statement.

```swift
let request = makeRequest(
    query: searchQuery,
    sortOrder: selectedSortOrder,
    includeArchived: shouldIncludeArchived,
    limit: maximumResultCount
)
```

## Function Declarations

For a wrapped parameter list, keep one parameter per line. This example keeps
effects and the return type with the closing parenthesis.

```swift
func loadItems(
    matching query: String,
    sortOrder: SortOrder,
    limit: Int
) async throws -> [Item] {
    try await store.fetch(query: query, sortOrder: sortOrder, limit: limit)
}
```

## Conditions

For a multiline guard, align the conditions and put `else` on its own line.
Keep a short guard on one line when that is the local convention.

```swift
guard
    let selectedItem = selection,
    selectedItem.isEditable,
    !isSaving
else {
    return
}
```

## Chained Calls

For a multiline chain, give each transformation its own line and indent the
chain one level. Do not expand a short expression solely to imitate this
example.

```swift
let titles = items
    .filter { $0.isVisible }
    .map { $0.title }
    .sorted()
```

## Trailing Closures

Keep a trailing closure attached to the call's closing parenthesis when the
argument list wraps. Indent the closure body one level.

```swift
loadItems(
    matching: searchQuery,
    limit: maximumResultCount
) { result in
    updateResults(result)
}
```
