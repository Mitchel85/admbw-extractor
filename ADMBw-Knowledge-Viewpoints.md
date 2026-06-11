# ADMBw Knowledge: Metamodell-Regeln pro Viewpoint

> **OpenWebUI Knowledge-Datei.** Enthält die erlaubten Elemente und Konnektoren für jeden Viewpoint.
> Extrahiert aus der ADMBw-Dokumentation v2025.10. Bei Fragen zur Viewpoint-Konformität: hier suchen.

## Concept Viewpoints

### C1 – Capability Taxonomy
**Erlaubte Elemente:**
- `Capability` (auf Class)
- `CapabilityGeneralization` (auf Generalization) — verbindet Capability→Capability
- `PropertySet` (abstrakt) — NICHT direkt verwenden
- `Measurement` (auf Class)
- `MeasurementType` (auf Class)
- `OwnsMeasurement` — verbindet MeasurableElement→Measurement
- `StrategicConstraint` (auf Class)
- `Satisfy` — verbindet Constraint→Element

### C2 – Enterprise Vision
**Erlaubte Elemente:**
- `EnterprisePhase` / `ActualEnterprisePhase` (auf Object)
- `TemporalPart` (auf Part)
- `WholeLifeEnterprise` (auf Class)
- `ResourceArchitecture` (auf Class)
- `EnterpriseVision` (auf Class)
- `ActualEnduringTask` (auf Object)
- `Capability` (auf Class)
- `CapabilityForTask` — verbindet Capability→EnduringTask
- `StrategicConstraint` (auf Class)
- `VisionForActualEnterprisePhase` — verbindet Vision→EnterprisePhase

### C3 – Capability Dependencies
**Erlaubte Elemente:**
- `Capability` (auf Class)
- `CapabilityDependency` (auf Dependency) — verbindet Capability→Capability

### C4 – Standard Processes
**Erlaubte Elemente:**
- `BusinessProcess` (auf Activity)
- `ProcessGeneralization` (auf Generalization)
- `ProcessEdge`, `ProcessOperation`, `ProcessParameter`, `ProcessUsage` (alle abstrakt)

### C5 – Effects
**Erlaubte Elemente:**
- `DesiredEffect` — verbindet Desirer→Effect
- `AchievedEffect` — verbindet Achiever→Effect
- `Desirer`, `Achiever` (auf Object)
- `ActualEnduringTask`, `EnduringTask`

### C7 – Performance Parameters
**Erlaubte Elemente:**
- `Measurement` (auf Class)
- `MeasurementType` (auf Class)
- `MeasurableElement` (abstrakt)
- `OwnsMeasurement`
- `ActualMeasurementSet`, `OwnsActualMeasurementSet`

### C8 – Planning Assumptions
**Erlaubte Elemente:**
- `ActualEnterprisePhase` (auf Object)
- `EnterpriseGoal` (auf Class)
- `Forecast` (auf Dependency)
- `ForecastPeriod` (auf Dependency)
- `SubjectOfForecast` (abstrakt)

### Cr – Capability Roadmap
**Erlaubte Elemente:**
- `Capability` (auf Class)
- `ActualEnterprisePhase` (auf Object)
- `Project` (abstrakt — siehe `ActualProject`)
- `ActualProjectMilestone`, `CapabilityConfiguration`

---

## Service Specification Viewpoints

### S1 – Service Taxonomy
**Erlaubte Elemente:**
- `ServiceSpecification` (auf Class)
- `ServiceSpecificationGeneralization` (auf Generalization)
- `ServiceSpecificationRole` (auf Part)
- `ServiceClassification` — verbindet ServiceSpecification→ServiceSpecificationRole

### S2 – Service Structure
**Erlaubte Elemente:**
- `ServiceSpecification` (auf Class)
- `ServiceSpecificationRole` (auf Part)
- `ServiceFunction` (abstrakt)
- `ServiceDependency` (auf Dependency)

### S3 – Service Interfaces
**Erlaubte Elemente:**
- `ServiceInterface` (auf Class)
- `ServicePort` (auf Port)
- `ServiceConnector` (auf InformationFlow)
- `ServiceMessage` (auf Message)
- `ServiceParameter` (auf Parameter)

### S4 – Service Functions
**Erlaubte Elemente:**
- `ServiceFunction` (auf Activity)
- `ServiceFunctionAction` (auf Action)
- `ServiceMethod` (auf Operation)
- `ServiceParameter` (auf Parameter)

### S5 – Service States
**Erlaubte Elemente:**
- `ServiceSpecification` (auf Class)
- `ServiceStateDescription` (auf StateMachine)

### S6 – Service Interactions
**Erlaubte Elemente:**
- `ServiceInterface`, `ServicePort`, `ServiceConnector`
- `ServiceMessage` (auf Message)
- `ServiceFunction` (abstrakt)
- `ServiceMethod` (auf Operation)

### S7 – Service Interface Parameters
**Erlaubte Elemente:**
- `ServiceParameter` (auf Parameter)
- `ServiceInterface` (auf Class)
- `ServicePort` (auf Port)

### S8 – Service Policy
**Erlaubte Elemente:**
- `ServicePolicy` (auf Class)
- `ServiceSpecification` (auf Class)
- `SecurityConstraint` (auf Constraint)

### Sr – Service Roadmap
**Erlaubte Elemente:**
- `ServiceSpecification`, `ActualEnterprisePhase`, `ActualProjectMilestone`

### C1-S1 – Capability to Service Mapping
**Erlaubte Elemente:**
- `Capability` (auf Class)
- `ServiceSpecification` (auf Class)
- `ServiceProvision` — verbindet Capability→ServiceSpecification

---

## Logical Specification Viewpoints

### L1 – Node Types
**Erlaubte Elemente:**
- `OperationalAgent` (abstrakt — verwende Subtypen)
- `OperationalNode` / `OpNode` (auf Class)
- `OperationalPort` (auf Port)
- `OperationalConnector` (auf Connector)
- `Location` (auf DataType)
- `OpNodeGeneralization` (auf Generalization)

### L2 – Logical Scenario
**Erlaubte Elemente:**
- `HighLevelOperationalConcept` (auf Class)
- `ConceptItem` (abstrakt) — NICHT direkt verwenden
- `ConceptRole` (auf Part) — Verwendung eines ConceptItem
- `OperationalAgent` (abstrakt)
- `ActualLocation` (auf Object)
- `OperationalActivity` (auf Activity)
- `ArbitraryConnector` (auf Dependency) — nur für High-Level-Konzeptverbindungen

### L3 – Node Interactions
**Erlaubte Elemente:**
- `OperationalNode`, `OperationalAgent`
- `OperationalConnector` / `Needline` (auf Connector)
- `OperationalExchange` (auf InformationFlow) — Fluss über Needline
- `InformationElement` (auf Class) — das, was ausgetauscht wird
- `ConveyedItem` — verknüpft Exchange mit InformationElement

### L4 – Logical Activities
**Erlaubte Elemente:**
- `OperationalActivity` (auf Activity)
- `StandardOperationalActivity` (auf Activity)
- `OperationalActivityAction` (auf Action) — Aufruf einer Activity in einer anderen
- `OperationalControlFlow` (auf ControlFlow)
- `OperationalObjectFlow` (auf ObjectFlow)
- `OperationalMessageFlow` (auf ControlFlow)
- `OperationalAgent` (abstrakt) — wer führt aus
- `ActivityPerformableUnderCondition` (auf Dependency)
- `ActsUpon` (auf Dependency) — Activity wirkt auf etwas
- `OperationalConstraint` (auf Constraint)

### L5 – Logical States
**Erlaubte Elemente:**
- `OperationalStateDescription` (auf Class)
- `OperationalAgent` (abstrakt)
- `ActualState` (abstrakt)

### L6 – Logical Sequence
**Erlaubte Elemente:**
- `OperationalAgent` (abstrakt)
- `OperationalActivity`, `StandardOperationalActivity`
- `OperationalExchange` (auf InformationFlow)
- `InteractionRole`, `InteractionMessage` (alle abstrakt)

### L7 – Information Model
**Erlaubte Elemente:**
- `InformationElement` (auf Class)
- `DataElement` (auf Class)
- `InformationElementGeneralization` (auf Generalization)
- `InformationElementComposition` (auf Aggregation)

### L8 – Logical Constraints
**Erlaubte Elemente:**
- `OperationalConstraint` (auf Constraint)
- `SubjectOfOperationalConstraint` (abstrakt)
- `Rule` (abstrakt) — verwende `OperationalConstraint`

### Lr – Lines of Development
**Erlaubte Elemente:**
- `ActualEnterprisePhase`, `OperationalAgent`, `ActualProject`

### L2-L3 – Logical Concept
**Erlaubte Elemente:**
- Kombination aus L2- und L3-Elementen

---

## Physical Resource Viewpoints

### P1 – Resource Types
**Erlaubte Elemente:**
- `ResourcePerformer` (abstrakt) — verwende: `System`, `Software`, `Technology`, `ResourceArtifact`, `ActualOrganization`, `ActualPerson`, `ActualPost`
- `ResourceRole` (auf Part)
- `TypicalResource` — verbindet ResourcePerformer→CapabilityConfiguration

### P2 – Resource Structure
**Erlaubte Elemente:**
- `ResourcePerformer` (abstrakt)
- `ResourceArtifact`, `Software`, `Technology`, `System`
- `ResourceRole` (auf Part)
- `ResourcePort` (auf Port)
- `ResourceConnector` (auf Connector)
- `ActualOrganization`, `ActualPerson`, `ActualPost`
- `CapabilityConfiguration` (auf Class)

### P3 – Resource Connectivity
**Erlaubte Elemente:**
- `ResourcePerformer` Subtypen
- `ResourcePort` (auf Port)
- `ResourceConnector` (auf Connector)
- `ResourceExchange` (auf InformationFlow)
- `ResourceExchangeItem` (abstrakt)
- `Protocol` (auf Class)
- `ProtocolLayer` (auf Part)
- `ResourceRole` (auf Part)

### P4 – Resource Functions
**Erlaubte Elemente:**
- `Function` (auf Activity)
- `FunctionAction` (auf Action)
- `FunctionControlFlow` (auf ControlFlow)
- `FunctionObjectFlow` (auf ObjectFlow)
- `ResourcePerformer` Subtypen
- `ResourceMethod` (auf Operation)

### P5 – Resource States
**Erlaubte Elemente:**
- `ResourceStateDescription` (auf StateMachine)
- `ResourcePerformer` Subtypen

### P6 – Resource Sequence
**Erlaubte Elemente:**
- `ResourcePerformer` Subtypen
- `ResourceExchange` (auf InformationFlow)
- `ResourceMessage` (auf Message)
- `ResourceMethod` (auf Operation)

### P7 – Data Model
**Erlaubte Elemente:**
- `DataModel` (auf Package)
- `DataElement` (auf Class)
- `DataRole` (auf Part)

### P8 – Resource Constraints
**Erlaubte Elemente:**
- `ResourceConstraint` (auf Class)
- `SubjectOfResourceConstraint` (abstrakt)
- `SecurityConstraint` (auf Constraint)
- `ResourceMitigation` (auf Class)

### Pr – Configuration Management
**Erlaubte Elemente:**
- `ActualProject`, `ResourcePerformer` Subtypen, `CapabilityConfiguration`

### L4-P4 – Activity to Function Mapping
**Erlaubte Elemente:**
- `OperationalActivity` → `Function` (Mapping)
- `MapsToCapability` — verbindet Activity→Capability

---

## Architecture Foundation

### A1 – Meta-Data Definitions
**Erlaubte Elemente:**
- `ArchitecturalDescription` (auf Package)
- `Metadata` (auf Note)
- `ArchitectureMetadata` (auf Note)

### A2 – Architecture Products
**Erlaubte Elemente:**
- `View` (auf Class)
- `Viewpoint` (auf Class)
- `ViewsInArchitecturalDescription`
- `ViewpointsInArchitecturalDescription`

### A3 – Architecture Correspondence
**Erlaubte Elemente:**
- `ArchitecturalReference` — verbindet Elemente über Viewpoints hinweg

### A4 – Methodology Used
**Erlaubte Elemente:**
- `ArchitecturalDescription` (auf Package) mit Tag `methodologyUsed`

### A5 – Architecture Status
**Erlaubte Elemente:**
- `ArchitecturalDescription` (auf Package) mit Tag `status`

### A6 – Architecture Versions
**Erlaubte Elemente:**
- `VersionOfConfiguration`, `VersionSuccession`, `VersionReleased`, `VersionWithdrawn`
- `VersionedElement` (abstrakt)

### A7 – Architecture Compliance
**Erlaubte Elemente:**
- `CompliesViewpoint` — verbindet View→Viewpoint
- `View`, `Viewpoint`

### A8 – Standards
**Erlaubte Elemente:**
- `Standard` (auf Class)
- `RatifiedStandards`, `ConformsTo`
- `Protocol` (auf Class)
- `IsEquivalentToStandardElement`, `ReplaceStandardElement`

### Ar – Architecture Roadmap
**Erlaubte Elemente:**
- `ArchitectureForProject`, `ActualEnterprisePhase`

---

## Requirement Viewpoints

### R2 – Requirement Catalogue
**Erlaubte Elemente:**
- `BWRequirement` (abstrakt) — verwende Subtypen
- `FunctionalRequirement`, `NonfunctionalRequirement` (auf Requirement)
- `RequirementCatalogue` (auf Class)
- `RequirementCategory` (auf Class)

### R3 – Requirement Dependencies
**Erlaubte Elemente:**
- `Requires` — verbindet Requirement→Requirement
- `ConflictsWith`, `Refines`, `DerivedFrom`

### R7 – Requirement Derivation
**Erlaubte Elemente:**
- `StemsFrom` — verbindet Requirement→Source
- `JustifiedBy`, `ResultsFrom`

### R8 – Requirement Fulfilment
**Erlaubte Elemente:**
- `RealiseRequirement` (auf Realisation) — verbindet Element→Requirement
- `Satisfy` — verbindet Element→Requirement
- `FulfilmentCriterion`, `FitCriterion`

### Rr – Requirement Realization
**Erlaubte Elemente:**
- `ToBeRealizedBy`, `RealizesRecommendation`, `RealizingAchievedEffect`
