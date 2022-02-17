---
id: api
title: API Reference
---
To make the usage simpler spacy provides custom extensions which a library can use. This makes it easier for the user to get the desired data. The below tables summaries the extensions.

## `spacy.Doc` extensions


| Extension | Type | Description | Default |
|-----------|------|-------------|---------|
| doc._.polarity | `Float` | The polarity of the document. The polarity score is a float within the range [-1.0, 1.0]. | `None` |
| doc._.subjectivity | `Float` | The subjectivity of the document. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. | `None` |
| doc._.assessments | `tuple` | Return a tuple of form (polarity, subjectivity, assessments ) where polarity is a float within the range [-1.0, 1.0], subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective, and assessments is a list of polarity and subjectivity scores for the assessed tokens. | `None` |


## `spacy.Span` extensions


| Extension | Type | Description | Default |
|-----------|------|-------------|---------|
| span._.polarity | `Float` | The polarity of the span. The polarity score is a float within the range [-1.0, 1.0]. | `None` |
| span._.subjectivity | `Float` | The subjectivity of the span. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. | `None` |
| span._.assessments | `tuple` | Return a tuple of form (polarity, subjectivity, assessments ) where polarity is a float within the range [-1.0, 1.0], subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective, and assessments is a list of polarity and subjectivity scores for the assessed tokens. | `None` |


## `spacy.Token` extensions


| Extension | Type | Description | Default |
|-----------|------|-------------|---------|
| token._.polarity | `Float` | The polarity of the token. The polarity score is a float within the range [-1.0, 1.0]. | `None` |
| token._.subjectivity | `Float` | The subjectivity of the token. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. | `None` |
| token._.assessments | `tuple` | Return a tuple of form (polarity, subjectivity, assessments ) where polarity is a float within the range [-1.0, 1.0], subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective, and assessments is a list of polarity and subjectivity scores for the assessed tokens. | `None` |
