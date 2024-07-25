                                                                                    Introduction
                                                                            #Review Terms - Chapter 0
 • Database-management system (DBMS).
 • Database-system applications.
 • Online transaction processing.
 • Dataanalytics.
 • File-processing systems.
 • Datainconsistency.
 • Consistency constraints.
 • Dataabstraction.
        ° Physical level.
        ° Logical level.
        ° View level.
 • Instance.
 • Schema.
        ° Physical schema.
        ° Logical schema.
        ° Subschema.
 • Physical data independence.
 • Datamodels.
        ° Entity-relationship model.
         ° Relational data model.
        ° Semi-structured data model.
        ° Object-based data model.
 • Database languages.
        ° Data-definition language.
        ° Data-manipulation language.
                 ⋄ Procedural DML.
                ⋄ Declarative DML.
                ⋄ nonprocedural DML.
        ° Query language.
 • Data-definition language.
        ° Domain Constraints.
        ° Referential Integrity.
        ° Authorization.
                ⋄ Read authorization.
                ⋄ Insert authorization.
                ⋄ Update authorization.
                ⋄ Delete authorization.
 • Metadata.
 • Application program.
 • Database design.
        ° Conceptual design.
        ° Normalization.
        ° Specification of functional requirements.
        ° Physical-design phase.
 • Database Engine.
        ° Storage manager.
                ⋄ Authorization and integrity manager.
                ⋄ Transaction manager.
                ⋄ File manager.
                ⋄ Buffer manager.
                ⋄ Data files.
                ⋄ Data dictionary.
                ⋄ Indices.
        ° Query processor.
                ⋄ DDL interpreter.
                ⋄ DML compiler.
                ⋄ Query optimization.
                ⋄ Query evaluation engine.
 ° Transactions.
        ⋄ Atomicity.
        ⋄ Consistency.
        ⋄ Durability.
        ⋄ Recovery manager.
        ⋄ Failure recovery.
        ⋄ Concurrency-control manager.
 • Database Architecture.
        ° Centralized.
        ° Parallel.
        ° Distributed.
 • Database Application Architecture.
        ° Two-tier.
        ° Three-tier.
        ° Application server.
 • Database administrator (DBA).
                                                                        #Practice Exercises - Chapter 0

 1.1 This chapter has described several major advantages of a database system. What
 are two disadvantages?

 1.2 List five ways in which the type declaration system of a language such as Java
 or C++ differs from the data definition language used in a database.

 1.3 List six major steps that you would take in setting up a database for a particular
 enterprise.

 1.4 Suppose you want to build a video site similar to YouTube. Consider each of the
 points listed in Section 1.2 as disadvantages of keeping data in a file-processing
 system. Discuss the relevance of each of these points to the storage of actual
 video data, and to metadata about the video,such as title,the user who uploaded
 it, tags, and which users viewed it.

 1.5 Keyword queries used in web search are quite different from database queries.
 List key differences between the two,in terms of the way the queries are specified
 and in terms of what is the result of a query.

                                                                            #Exercises - Chapter 0

1.6 List four applications you have used that most likely employed a database system
to store persistent data.

 1.7 List four significant differences between a file-processing system and a DBMS.

 1.8 Explain the concept of physical data independence and its importance in
 database systems.

 1.9 List five responsibilities of a database-management system. For each responsi
bility, explain the problems that would arise if the responsibility were not dis
charged.

 1.10 List at least two reasons why database systems support data manipulation using
 a declarative query language such as SQL, instead of just providing a library of
 Cor C++ functions to carry out data manipulation.

 1.11 Assume that two students are trying to register for a course in which there is only
 one open seat. What component of a database system prevents both students
 from being given that last seat?

 1.12 Explain the difference between two-tier and three-tier application architectures.
 Which is better suited for web applications? Why?
        
 1.13 List two features developed in the 2000s and that help database systems handle
 data-analytics workloads.

 1.14 Explain why NoSQL systems emerged in the 2000s, and briefly contrast their
 features with traditional database systems.

 1.15 Describeat least three tables that might be used to store information in a social
networking system such as Facebook.
