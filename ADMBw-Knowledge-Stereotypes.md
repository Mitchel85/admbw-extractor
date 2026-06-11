# ADMBw Knowledge: Stereotype-Katalog (317 Stereotype)

> **OpenWebUI Knowledge-Datei.** Enthält alle 317 ADMBw-Stereotype mit AppliesTo und TaggedValues.
> Bei Unsicherheit über einen Stereotypen: hier semantisch suchen.

## Regel: Ein Stereotyp darf NUR auf die gelisteten Metaclasses angewendet werden.

| Stereotype | AppliesTo (EA-Metaclass) | Tags |
|-----------|-------------------------|------|
| `AchievedEffect` | Dependency | |
| `Achiever` | Object | |
| `ActivityPerformableUnderCondition` | Dependency | |
| `ActivitySupportsService` | Realisation | |
| `ActsUpon` | Dependency | |
| `ActualCondition` | Object | |
| `ActualConditionToActualResource` | Dependency | |
| `ActualEnduringTask` | Object | |
| `ActualEnterprisePhase` | Object | endDate, startDate |
| `ActualEnvironment` | Object | AbstractionLevel |
| `ActualLocation` | Object | address, customKind, locationNamedByAddress, locationKind, AbstractionLevel |
| `ActualMeasurement` | Slot | intention |
| `ActualMeasurementSet` | Object | |
| `ActualMeasurementSetAppliesFor` | Dependency | |
| `ActualOrganization` | Object | shortName, serviceType |
| `ActualOrganizationRole` | Slot | |
| `ActualOrganizationalResource` 🔒 | Object | |
| `ActualPerson` | Object | |
| `ActualPost` | Object | |
| `ActualProject` | Object | endDate, startDate, projectKind, project-ID, projectShortTitle |
| `ActualProjectConsults` | Dependency | |
| `ActualProjectDependency` | Dependency | |
| `ActualProjectInforms` | Dependency | |
| `ActualProjectMilestone` | Object | endDate, startDate, kind, projectStatus |
| `ActualProjectMilestoneRole` | Slot | |
| `ActualPropertySet` | Object | |
| `ActualResource` | Object | |
| `ActualResourceNeededByActualProjectMilestone` | Dependency | |
| `ActualResourceRelationship` | InformationFlow | |
| `ActualResourceRole` | Slot | |
| `ActualResourceToActualProjectMilestone` | Dependency | |
| `ActualResponsibleResource` 🔒 | Object | |
| `ActualService` | Object | |
| `ActualServiceSpecificationRole` | Slot | |
| `ActualState` 🔒 | Object | endDate, startDate |
| `AffectedActivity` | Dependency | |
| `AffectedFunctions` | Dependency | |
| `AffectedResource` | Dependency | |
| `Alias` | Note | |
| `ArbitraryConnector` | Dependency | |
| `ArchitecturalDescription` | Package | status, version, methodologyUsed, approvalAuthority, architect, assumptionAndConstraint +9 |
| `ArchitecturalReference` | Dependency | |
| `ArchitecturalSequence` | Dependency | |
| `Architecture` 🔒 | Class | AbstractionLevel |
| `ArchitectureForProject` | Dependency | |
| `ArchitectureMetadata` | Note | |
| `Asset` 🔒 | Class | AbstractionLevel |
| `AssetRole` 🔒 | Part | |
| `BWRequirement` 🔒 | Requirement | Uuid, Afo_ID, AG_ID, Akteur, Anforderungsart, Ansprechpartner +33 |
| `BoundaryCondition` | Dependency | |
| `BusinessProcess` 🔒 | Activity | AbstractionLevel |
| `Capability` | Class | Status, AbstractionLevel |
| `CapabilityConfiguration` | Class | Avoiding redundancy in IT-SysBw, Avoids provider monopoly, Client separation, Environmentally friendly and sustainable, Fulfilled C5 requirements catalogue of the BSI, Geodata and geoservices +10 |
| `CapabilityDependency` | Dependency | |
| `CapabilityForTask` | Abstraction | |
| `CapabilityGeneralization` | Generalization | |
| `CapabilityRole` | Part | AbstractionLevel |
| `CapabilityRoleDependency` | Dependency | |
| `CapableElement` 🔒 | CapableElement | |
| `Checks` | Dependency | |
| `Classification` | Class | Definition, Responsibility |
| `Classified` | Dependency | |
| `Command` | InformationFlow | |
| `Competence` | Class | ATB, ATN, AVR |
| `CompetenceForRole` | Dependency | |
| `CompliesViewpoint` | Dependency | |
| `ConceptItem` 🔒 | ConceptItem | |
| `ConceptRole` | Part | |
| `Concern` | Class | |
| `ConcernForActualEnterprisePhase` | Dependency | |
| `ConcernForView` | Dependency | |
| `ConcernForViewpoint` | Dependency | |
| `Condition` | Class, DataType | |
| `ConflictsWith` | Dependency | |
| `ConformsTo` | Dependency | |
| `ConsumedBy` | Dependency | |
| `Consumes` | Abstraction | |
| `Control` | InformationFlow | |
| `DataElement` | Class | AbstractionLevel |
| `DataElementStoredIn` | Dependency | |
| `DataModel` | Package | kind, AbstractionLevel |
| `DataRole` | Part | |
| `Definition` | Note | |
| `DerivedFrom` | Dependency | |
| `DescribedBy` | Dependency | |
| `DesiredEffect` | Dependency | |
| `Desirer` 🔒 | Desirer | |
| `DocumentReference` | Class | |
| `ElementCatalogue` | Package | |
| `EnduringTask` | Class | |
| `Energy` | Class | |
| `EnterpriseGoal` | Class | benefits, AbstractionLevel |
| `EnterprisePhase` | Class | toBe, AbstractionLevel |
| `EnterpriseVision` | Class | AbstractionLevel |
| `Environment` | Class | kind, AbstractionLevel |
| `EnvironmentProperty` | Class | AbstractionLevel |
| `EnvironmentalCondition` | Dependency | |
| `EnvironmentalContext` | Dependency | |
| `Evaluates` | Realisation | |
| `Exchange` 🔒 | Exchange | |
| `ExchangeItem` 🔒 | ExchangeItem | AbstractionLevel |
| `Exhibits` | Abstraction | |
| `Expresses` | Dependency | |
| `FieldedCapability` | Object | AbstractionLevel |
| `FillsPost` | Dependency | |
| `Finding` | Class | Type |
| `FitCriterion` | Class | text |
| `Forecast` | Dependency | |
| `ForecastPeriod` | Dependency | |
| `FormStoredIn` | Dependency | |
| `FulfilmentCriterion` | Class | text |
| `Function` | Activity | AbstractionLevel |
| `FunctionAction` | Action | |
| `FunctionControlFlow` | ControlFlow | |
| `FunctionEdge` | FunctionEdge | |
| `FunctionObjectFlow` | ObjectFlow | |
| `FunctionSubject` | Dependency | |
| `FunctionalRequirement` | Requirement | |
| `GeoPoliticalExtentType` | DataType | kind, customKind |
| `GoalForActualEnterprisePhase` | Dependency | |
| `HighLevelOperationalConcept` | Class | |
| `HostedOn` | Dependency | |
| `Implements` 🔒 | Abstraction | |
| `ImplementsProtocol` | Dependency | |
| `Information` | Note | informationKind |
| `InformationElement` | Class | Event, Eventtriggered, AmountOfInformation, ConfirmationRequired, DeviceControl, Frequency +11 |
| `InformationRole` | Part | |
| `InteractionMessage` 🔒 | Message | |
| `InteractionRole` 🔒 | Lifeline | |
| `IsAccountableFor` | Dependency | |
| `IsCapableToPerform` | Abstraction | |
| `IsDuplicateOf` | Dependency | |
| `IsEquivalentToStandardElement` | Dependency | |
| `IsResponsibleFor` | Dependency | |
| `JustifiedBy` | Dependency | |
| `KnownResource` | Class | |
| `Location` | Class, DataType | customKind, kind |
| `LocationHolder` 🔒 | LocationHolder | |
| `LocationType` | Dependency | |
| `MapsToCapability` | Abstraction | |
| `MeasurableElement` 🔒 | MeasurableElement | |
| `Measurement` | Part | ITSD_ServiceClass |
| `MeasurementType` | Class | ITSD_Group |
| `Metadata` | Note | dublinCoreElement, metaDataScheme, name, category |
| `MilestoneDependency` | Dependency | |
| `NaturalResource` | Class | |
| `NeedsModificationOf` | Dependency | |
| `NeedsResource` | Dependency | |
| `NeedsService` | Dependency | |
| `NonfunctionalRequirement` | Requirement | |
| `OperationalActivity` | Activity | AbstractionLevel |
| `OperationalActivityAction` | Action, Activity | |
| `OperationalActivityEdge` | OperationalActivityEdge | |
| `OperationalAgent` 🔒 | Class | |
| `OperationalArchitecture` | Class | |
| `OperationalArchitectureOfEnterprisePhase` | Dependency | |
| `OperationalAsset` 🔒 | Class | AbstractionLevel |
| `OperationalConnector` | Connector | |
| `OperationalConstraint` | Class | Id, Uuid, AbstractionLevel |
| `OperationalControlFlow` | ControlFlow | |
| `OperationalExchange` | InformationFlow | exchangeKind |
| `OperationalExchangeItem` 🔒 | OperationalExchangeItem | |
| `OperationalInterface` | Class | |
| `OperationalMessage` | Message | |
| `OperationalMessageFlow` | ControlFlow | |
| `OperationalMethod` | Operation | |
| `OperationalObjectFlow` | ObjectFlow | |
| `OperationalParameter` | Parameter | |
| `OperationalPerformer` | Class | Nationality, SizeIndicator |
| `OperationalPort` | Port | |
| `OperationalRole` | Part | Nationality, SizeIndicator |
| `OperationalSignal` | Signal | |
| `OperationalSignalProperty` | Part | |
| `OperationalStateDescription` | Class | |
| `Organization` | Class | |
| `OrganizationalResource` 🔒 | Class | |
| `OriginatesFrom` | Dependency | |
| `OwnedMilestone` | Dependency | |
| `OwnsActualMeasurementSet` | Dependency | |
| `OwnsMeasurement` | Dependency | |
| `OwnsProcess` | Abstraction | |
| `PaperForm` | Class | |
| `PartOfCatalogue` | Aggregation | |
| `PartOfCategory` | Aggregation | |
| `PerformsInContext` | Abstraction | |
| `Person` | Class | |
| `PhysicalArchitectureOfEnterprisePhase` | Dependency | |
| `PhysicalLocation` | Dependency | |
| `PhysicalResource` 🔒 | Class | |
| `Post` | Class | |
| `PostRole` | Part | |
| `ProblemDomain` | Part | |
| `ProcessEdge` 🔒 | ProcessEdge | |
| `ProcessGeneralization` | Generalization | |
| `ProcessMessageFlow` | ProcessMessageFlow | |
| `ProcessOperation` 🔒 | ProcessOperation | |
| `ProcessParameter` 🔒 | ProcessParameter | |
| `ProcessUsage` 🔒 | ProcessUsage | |
| `Project` | Class | Architectural guidelines of the Federal Government, Catalogue usage, Criteria of architecture quality fulfilled, Implemented SASPF specification, Implementing Change Management, Modeling according to PlgABw +14 |
| `ProjectMilestone` | Class | |
| `ProjectMilestoneRole` | Part | |
| `ProjectMilestoneToProjectTheme` | Dependency | |
| `ProjectProvidesFunction` | Dependency | |
| `ProjectRole` | Part | |
| `ProjectSequence` | Dependency | |
| `ProjectStatus` | Slot | |
| `ProjectSupportActivity` | Dependency | |
| `ProjectTheme` | Part | status |
| `PropertySet` 🔒 | PropertySet | |
| `PropertySetGeneralization` | Generalization | |
| `Protocol` | Class | |
| `ProtocolImplementation` 🔒 | ProtocolImplementation | |
| `ProtocolLayer` | Part | |
| `Protocolstack` | Class | |
| `ProvidedServiceLevel` | Object | |
| `Provides` | Dependency | |
| `ProvidesCompetence` | Dependency | |
| `ProvidesServiceFunction` | Dependency | |
| `RatifiedStandards` | Dependency | |
| `RealiseRequirement` | Realisation | |
| `RealizedDesiredEffect` | Dependency | |
| `RealizesRecommendation` | Realisation | |
| `RealizingAchievedEffect` | Dependency | |
| `Recommendation` | Class | Type |
| `Reference` | Class | Date |
| `RefersTo` | Dependency | |
| `Refines` | Dependency | |
| `ReplaceStandardElement` | Dependency | |
| `Replaces` | Dependency | |
| `RequiredEnvironment` | Dependency | |
| `RequiredResource` | Dependency | |
| `RequiredServiceLevel` | Object | |
| `RequirementCatalogue` | Class | |
| `RequirementCategory` | Class | |
| `Requires` | Dependency | |
| `RequiresCompetence` | Abstraction | |
| `Resource` 🔒 | Resource | |
| `ResourceArchitecture` | Class | materialPlanningNumber |
| `ResourceArtifact` | Class | Scalability, Scaling method, Type of scalability, materialPlanningNumber |
| `ResourceAsset` 🔒 | Class | |
| `ResourceConnector` | Connector | Bandwidth |
| `ResourceConstraint` | Class | |
| `ResourceDependency` | Dependency | |
| `ResourceExchange` | InformationFlow | exchangeKind |
| `ResourceExchangeItem` 🔒 | ResourceExchangeItem | |
| `ResourceInterface` | Class | |
| `ResourceMessage` | Message | |
| `ResourceMethod` | Operation | |
| `ResourceMitigation` | Class | |
| `ResourceParameter` | Parameter | |
| `ResourcePerformer` 🔒 | Class | AbstractionLevel |
| `ResourcePort` | Port | Richardson Maturity Model |
| `ResourceRole` | Part | roleKind, Virtualization level, Virtualization location, SecurityDomain, IT security accreditation, Programming language +1 |
| `ResourceSignal` | Signal | |
| `ResourceSignalProperty` | Part | |
| `ResourceStateDescription` | StateMachine | |
| `ResourceToServiceDependency` | Dependency | |
| `Responsibility` | Class | |
| `Responsible` | Dependency | |
| `ResultsFrom` | Dependency | Type |
| `Rule` 🔒 | Constraint | ruleKind |
| `SMEReference` | Class | |
| `SameAs` | Dependency | |
| `Satisfy` | Dependency | |
| `SecurityConstraint` | Constraint | |
| `SecurityEnclave` | Class | |
| `SecurityProcess` | Activity | |
| `ServiceClassification` | Dependency | AbstractionLevel |
| `ServiceConnector` | InformationFlow | |
| `ServiceDependency` | Dependency | |
| `ServiceFunction` 🔒 | Activity | AbstractionLevel, ITSD_UtilityUsage |
| `ServiceFunctionAction` | Action | |
| `ServiceInterface` | Class | |
| `ServiceMessage` | Message | |
| `ServiceMethod` | Operation | |
| `ServiceParameter` | Parameter | |
| `ServicePolicy` | Class | |
| `ServicePort` | Port | |
| `ServiceProvision` | Abstraction | |
| `ServiceSpecification` | Class | Approved service tailoring, Critical service, Kind of robustness, Measure for robustness, Minimization of dependencies, Service with mission reference +2 |
| `ServiceSpecificationGeneralization` | Generalization | |
| `ServiceSpecificationRole` | Part | |
| `ServiceStateDescription` | StateMachine | |
| `Software` | Class | Role model in IAM, Scalable (on infrastructure), Scaling method |
| `Stakeholder` | Stakeholder | |
| `StakeholderConcern` | Dependency | |
| `Standard` | Class | mandatedDate, retiredDate, AbstractionLevel |
| `StandardOperationalActivity` | Activity | |
| `StateDescription` 🔒 | StateMachine | |
| `StatementTask` | Dependency | |
| `StemsFrom` | Dependency | |
| `StoredIn` | Dependency | originalSource |
| `StrategicConstraint` | Class | |
| `SubOrganization` | Part | |
| `SubjectOfForecast` 🔒 | Class | |
| `SubjectOfOperationalConstraint` 🔒 | SubjectOfOperationalConstraint | |
| `SubjectOfResourceConstraint` 🔒 | SubjectOfResourceConstraint | |
| `SubjectOfSecurityConstraint` 🔒 | SubjectOfSecurityConstraint | |
| `SuccessorOf` | Dependency | |
| `System` | Class | |
| `Technology` | Class | |
| `TemporalPart` | Part | |
| `ToBeRealizedBy` | Dependency | |
| `UAFElement` 🔒 | UAFElement | URI |
| `VersionOfConfiguration` | Part | |
| `VersionReleased` | Dependency | |
| `VersionSuccession` | Dependency | |
| `VersionWithdrawn` | Dependency | |
| `VersionedElement` 🔒 | VersionedElement | |
| `View` | Class | MachineReadable, AbstractionLevel |
| `Viewpoint` | Class | purpose, language, method, AbstractionLevel |
| `ViewpointToStakeholder` | Dependency | |
| `ViewpointsInArchitecturalDescription` | Dependency | |
| `ViewsInArchitecturalDescription` | Dependency | |
| `VisionForActualEnterprisePhase` | Dependency | |
| `WholeLifeConfiguration` | Class | kind |
| `WholeLifeEnterprise` | Class | |

## Abstrakte Stereotype (42 — NIEMALS DIREKT VERWENDEN)

Diese Stereotype sind abstrakt. Nur ihre Subtypen dürfen verwendet werden:

- `ActualOrganizationalResource` → Object
- `ActualResponsibleResource` → Object
- `ActualState` → Object
- `Architecture` → Class
- `Asset` → Class
- `AssetRole` → Part
- `BWRequirement` → Requirement
- `BusinessProcess` → Activity
- `CapableElement` → CapableElement
- `ConceptItem` → ConceptItem
- `Desirer` → Desirer
- `Exchange` → Exchange
- `ExchangeItem` → ExchangeItem
- `Implements` → Abstraction
- `InteractionMessage` → Message
- `InteractionRole` → Lifeline
- `LocationHolder` → LocationHolder
- `MeasurableElement` → MeasurableElement
- `OperationalAgent` → Class
- `OperationalAsset` → Class
- `OperationalExchangeItem` → OperationalExchangeItem
- `OrganizationalResource` → Class
- `PhysicalResource` → Class
- `ProcessEdge` → ProcessEdge
- `ProcessOperation` → ProcessOperation
- `ProcessParameter` → ProcessParameter
- `ProcessUsage` → ProcessUsage
- `PropertySet` → PropertySet
- `ProtocolImplementation` → ProtocolImplementation
- `Resource` → Resource
- `ResourceAsset` → Class
- `ResourceExchangeItem` → ResourceExchangeItem
- `ResourcePerformer` → Class
- `Rule` → Constraint
- `ServiceFunction` → Activity
- `StateDescription` → StateMachine
- `SubjectOfForecast` → Class
- `SubjectOfOperationalConstraint` → SubjectOfOperationalConstraint
- `SubjectOfResourceConstraint` → SubjectOfResourceConstraint
- `SubjectOfSecurityConstraint` → SubjectOfSecurityConstraint
- `UAFElement` → UAFElement
- `VersionedElement` → VersionedElement

## MDG-Errata (Tippfehler)

| MDG-Wert (falsch) | Korrekt |
|-------------------|---------|
| `ProviededServiceLevel` | `ProvidedServiceLevel` |
| `ActualMeasurementSetAppiesFor` | `ActualMeasurementSetAppliesFor` |
| `VersionSucession` | `VersionSuccession` |
