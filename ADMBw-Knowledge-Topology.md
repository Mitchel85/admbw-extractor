# ADMBw Knowledge: Metamodell-Topologie pro Viewpoint

> **Gerichtete Kanten (Source→Connector→Target) für jeden Viewpoint.**
> Extrahiert aus `NAFv4-ADMBw-MDG-2025.10.xml` (`<metaconstraints>`).
> Querverweis: `ADMBw-Knowledge-Viewpoints.md` (erlaubte Elemente).

| Feld | Bedeutung |
|------|-----------|
| Source | client/source — der Ausgangspunkt des Pfeils |
| Connector | Der NAF-Konnektor-Stereotyp |
| Target | supplier/target — das Ziel des Pfeils |
| `;` | Trenner für mehrere erlaubte Typen (ODER) |

## 🏛️ Concept

### C1 – Capability Taxonomy
- `Capability` → **CapabilityGeneralization** → `Capability`
- `MeasurableElement` → **OwnsMeasurement** → `Measurement; MeasurementType`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### C2 – Enterprise Vision
- `Capability` → **CapabilityForTask** → `ActualEnduringTask; EnduringTask`
- `Exhibits` → **EnvironmentalCondition** → `Environment`
- `CapableElement` → **Exhibits** → `Capability`
- `ActualEnterprisePhase` → **GoalForActualEnterprisePhase** → `EnterpriseGoal`
- `ActualEnterprisePhase` → **OperationalArchitectureOfEnterprisePhase** → `OperationalArchitecture`
- `ActualEnterprisePhase` → **PhysicalArchitectureOfEnterprisePhase** → `ResourceArchitecture`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`
- `ActualEnterprisePhase` → **StatementTask** → `ActualEnduringTask`
- `ActualEnterprisePhase` → **VisionForActualEnterprisePhase** → `EnterpriseVision`

### C3 – Capability Dependencies
- `Capability` → **CapabilityDependency** → `Capability`
- `Capability` → **CapabilityGeneralization** → `Capability`
- `CapabilityRole` → **CapabilityRoleDependency** → `CapabilityRole`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### C4 – Standard Processes
- `Capability` → **CapabilityForTask** → `ActualEnduringTask; EnduringTask`
- `BusinessProcess` → **MapsToCapability** → `Capability`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### C5 – Effects
- `Achiever` → **AchievedEffect** → `ActualState`
- `Desirer` → **DesiredEffect** → `ActualState`
- `Exhibits` → **EnvironmentalCondition** → `Environment`
- `CapableElement` → **Exhibits** → `Capability`
- `AchievedEffect` → **RealizedDesiredEffect** → `DesiredEffect`
- `DesiredEffect` → **RealizingAchievedEffect** → `AchievedEffect`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### C7 – Performance Parameters
- `MeasurableElement` → **OwnsMeasurement** → `Measurement; MeasurementType`

### C8 – Planning Assumption
- `ActualProject` → **ActualProjectDependency** → `ActualProject`
- `ActualResource` → **ActualResourceNeededByActualProjectMilestone** → `ActualProjectMilestone`
- `ActualResource` → **ActualResourceToActualProjectMilestone** → `ActualProjectMilestone`
- `Exhibits` → **EnvironmentalCondition** → `Environment`
- `CapableElement` → **Exhibits** → `Capability`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint` → **JustifiedBy** → `Reference`
- `ActualProjectMilestone` → **MilestoneDependency** → `ActualProjectMilestone`
- `ActualProject` → **OwnedMilestone** → `ActualProjectMilestone`
- `ProjectMilestone` → **ProjectMilestoneToProjectTheme** → `ProjectTheme`
- `ActualProject` → **ProjectSequence** → `ActualProject`
- `ProjectMilestone` → **RequiredResource** → `ResourcePerformer`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`
- `ActualProjectMilestone` → **VersionReleased** → `VersionedElement`
- `ActualProjectMilestone` → **VersionWithdrawn** → `VersionedElement`

## 🏛️ Service

### S1 – Service Taxonomy
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`
- `ServiceSpecification` → **ServiceClassification** → `ServiceSpecification`
- `ServiceSpecification` → **ServiceSpecificationGeneralization** → `ServiceSpecification`

### S2 – Service Structure
- `Organization` → **IsAccountableFor** → `ActualProject; ResourcePerformer; ServiceSpecification`
- `Organization` → **IsResponsibleFor** → `ActualProject; ResourcePerformer; ServiceSpecification`
- `ServiceInterface` → **ProvidesServiceFunction** → `ServiceFunction`
- `ServiceSpecification` → **ServiceDependency** → `OperationalAgent; ResourcePerformer; ServiceSpecification`

### S3 – Service Interfaces
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### S4 – Service Functions
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### S6 – Service Interactions
- `OperationalActivity` → **OperationalExchange** → `OperationalActivity`

### S7 – Service Interface Parameters
- `ServiceInterface` → **ProvidesServiceFunction** → `ServiceFunction`

### S8 – Service Policy
- `ActualProject` → **ActualProjectDependency** → `ActualProject`
- `Exhibits` → **EnvironmentalCondition** → `Environment`
- `CapableElement` → **Exhibits** → `Capability`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `Organization` → **IsAccountableFor** → `ActualProject; ResourcePerformer; ServiceSpecification`
- `Organization` → **IsResponsibleFor** → `ActualProject; ResourcePerformer; ServiceSpecification`
- `ActualProjectMilestone` → **MilestoneDependency** → `ActualProjectMilestone`
- `ActualProject` → **NeedsService** → `ServiceSpecification; ServiceSpecificationRole`
- `ActualProject` → **OwnedMilestone** → `ActualProjectMilestone`
- `ProjectMilestone` → **ProjectMilestoneToProjectTheme** → `ProjectTheme`
- `ActualProject` → **ProjectSequence** → `ActualProject`
- `ProjectMilestone` → **RequiredResource** → `ResourcePerformer`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`
- `ActualProjectMilestone` → **VersionReleased** → `VersionedElement`
- `ActualProjectMilestone` → **VersionWithdrawn** → `VersionedElement`

## 🏛️ Logical

### L1 – Node Types
- `Exhibits` → **EnvironmentalCondition** → `Environment`
- `CapableElement` → **Exhibits** → `Capability`
- `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint` → **JustifiedBy** → `Reference`
- `BusinessProcess` → **MapsToCapability** → `Capability`
- `MeasurableElement` → **OwnsMeasurement** → `Measurement; MeasurementType`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### L2 – Logical Scenario
- `ServiceSpecification; ServiceSpecificationRole` → **ConsumedBy** → `OperationalPerformer; OperationalRole`
- `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint` → **JustifiedBy** → `Reference`
- `LocationHolder` → **LocationHolder** → `Location`
- `OperationalActivity` → **OperationalExchange** → `OperationalActivity`
- `MeasurableElement` → **OwnsMeasurement** → `Measurement; MeasurementType`
- `LocationHolder` → **PhysicalLocation** → `ActualLocation`
- `OperationalPerformer; OperationalRole` → **Provides** → `ServiceSpecification; ServiceSpecificationRole`
- `LocationHolder` → **RequiredEnvironment** → `ActualEnvironment`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### L3 – Node Interaction
- `ServiceSpecification; ServiceSpecificationRole` → **ConsumedBy** → `OperationalPerformer; OperationalRole`
- `OperationalActivity` → **OperationalExchange** → `OperationalActivity`
- `MeasurableElement` → **OwnsMeasurement** → `Measurement; MeasurementType`
- `OperationalPerformer; OperationalRole` → **Provides** → `ServiceSpecification; ServiceSpecificationRole`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### L4 – Logical Activities
- `BusinessProcess` → **ActivityPerformableUnderCondition** → `ActualCondition`
- `OperationalActivity` → **ActivitySupportsService** → `ServiceSpecification`
- `OperationalActivity; OperationalActivityAction` → **ActsUpon** → `OperationalExchangeItem; PaperForm`
- `OperationalExchangeItem` → **AffectedActivity** → `OperationalActivity`
- `OperationalActivity` → **AffectedResource** → `OperationalExchangeItem`
- `OperationalActivity; OperationalActivityAction` → **Consumes** → `ActualService; ServiceSpecification`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint` → **JustifiedBy** → `Reference`
- `OperationalActivity` → **OperationalExchange** → `OperationalActivity`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### L6 – Logical Sequence
- `OperationalActivity` → **OperationalExchange** → `OperationalActivity`

### L7 – Information Model
- `ArchitecturalDescription; DataElement; DocumentReference; InformationElement; ServiceSpecification` → **Classified** → `Classification`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint` → **JustifiedBy** → `Reference`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### L8 – Logical Constraints
- `ActualProject` → **ActualProjectConsults** → `Organization`
- `ActualProject` → **ActualProjectDependency** → `ActualProject`
- `ActualProject` → **ActualProjectInforms** → `Organization`
- `ConceptRole` → **ArbitraryConnector** → `ConceptRole`
- `ActualProject; ActualProjectMilestone` → **ArchitectureForProject** → `ArchitecturalDescription`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `Organization` → **IsAccountableFor** → `ActualProject; ResourcePerformer; ServiceSpecification`
- `Organization` → **IsResponsibleFor** → `ActualProject; ResourcePerformer; ServiceSpecification`
- `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint` → **JustifiedBy** → `Reference`
- `ActualProjectMilestone` → **MilestoneDependency** → `ActualProjectMilestone`
- `OperationalActivity` → **OperationalExchange** → `OperationalActivity`
- `ActualProject` → **OwnedMilestone** → `ActualProjectMilestone`
- `ProjectMilestone` → **ProjectMilestoneToProjectTheme** → `ProjectTheme`
- `ActualProject` → **ProjectSequence** → `ActualProject`
- `ProjectMilestone` → **RequiredResource** → `ResourcePerformer`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`
- `ActualProjectMilestone` → **VersionReleased** → `VersionedElement`
- `ActualProjectMilestone` → **VersionWithdrawn** → `VersionedElement`

## 🏛️ Physical

### P1 – Resource Types
- `DataElement` → **DataElementStoredIn** → `ResourcePerformer; ResourceRole`
- `SubjectOfForecast` → **Forecast** → `SubjectOfForecast`
- `Forecast` → **ForecastPeriod** → `ActualEnterprisePhase`
- `PaperForm` → **FormStoredIn** → `Software`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `MeasurableElement` → **OwnsMeasurement** → `Measurement; MeasurementType`
- `OrganizationalResource` → **RequiresCompetence** → `Competence`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`
- `ActualResource; ResourcePerformer; ResourceRole` → **ServiceProvision** → `ActualService; ServiceSpecification; ServiceSpecificationRole`

### P2 – Resource Structure
- `ActualProject` → **ActualProjectConsults** → `Organization`
- `ActualProject` → **ActualProjectInforms** → `Organization`
- `ResourceRole` → **CompetenceForRole** → `Competence`
- `ResourceArchitecture; ResourceArtifact; ResourceRole` → **HostedOn** → `ResourceArchitecture; ResourceArtifact; ResourceRole`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `Organization` → **IsAccountableFor** → `ActualProject; ResourcePerformer; ServiceSpecification`
- `Organization` → **IsResponsibleFor** → `ActualProject; ResourcePerformer; ServiceSpecification`
- `LocationHolder` → **LocationHolder** → `Location`
- `ActualProject` → **NeedsModificationOf** → `PhysicalResource; ResourceArchitecture; ResourceRole`
- `ActualProject` → **NeedsResource** → `PhysicalResource; ResourceArchitecture; ResourceRole`
- `LocationHolder` → **PhysicalLocation** → `ActualLocation`
- `ActualProject` → **ProjectProvidesFunction** → `Function`
- `ActualProject` → **ProjectSupportActivity** → `OperationalActivity`
- `LocationHolder` → **RequiredEnvironment** → `ActualEnvironment`
- `ResourcePerformer; ResourcePort; ResourceRole` → **ResourceDependency** → `ResourcePerformer; ResourcePort; ResourceRole`
- `ResourcePerformer; ResourceRole` → **ResourceToServiceDependency** → `ServiceSpecification; ServiceSpecificationRole`
- `ActualProject` → **Responsible** → `PhysicalResource; ResourceArchitecture; ResourceRole; ServiceSpecification`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`
- `ActualResource; ResourcePerformer; ResourceRole` → **ServiceProvision** → `ActualService; ServiceSpecification; ServiceSpecificationRole`

### P3 – Resource Connectivity
- `ProtocolImplementation` → **ImplementsProtocol** → `Protocol`
- `MeasurableElement` → **OwnsMeasurement** → `Measurement; MeasurementType`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### P4 – Resource Functions
- `ResourceExchangeItem` → **AffectedFunctions** → `Function`
- `Function` → **FunctionSubject** → `ResourceExchangeItem`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `MeasurableElement` → **OwnsMeasurement** → `Measurement; MeasurementType`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### P7 – Data Model
- `ArchitecturalDescription; DataElement; DocumentReference; InformationElement; ServiceSpecification` → **Classified** → `Classification`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint` → **JustifiedBy** → `Reference`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`

### P8 – Resource Constraints
- `ActualProject` → **ActualProjectDependency** → `ActualProject`
- `ActualPerson` → **FillsPost** → `ActualPost`
- `DataElement; Function; InformationElement; OperationalActivity; OperationalActivityAction; OperationalConstraint; ResourceConnector; ResourceConstraint; ResourceExchange; ResourceInterface; ResourcePerformer; ResourceRole; ServicePolicy` → **Implements** → `ActualEnduringTask; InformationElement; OperationalActivity; OperationalActivityAction; OperationalAgent; OperationalConnector; OperationalConstraint; OperationalExchange; OperationalInterface; OperationalRole; ResourceConnector; ServiceFunction; ServiceInterface; ServicePolicy; StrategicConstraint`
- `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint` → **JustifiedBy** → `Reference`
- `ActualProjectMilestone` → **MilestoneDependency** → `ActualProjectMilestone`
- `ActualProject` → **OwnedMilestone** → `ActualProjectMilestone`
- `ProjectMilestone` → **ProjectMilestoneToProjectTheme** → `ProjectTheme`
- `ActualProject` → **ProjectSequence** → `ActualProject`
- `ProjectMilestone` → **RequiredResource** → `ResourcePerformer`
- `Capability; OperationalActivityAction; ServiceSpecification; SubjectOfOperationalConstraint; SubjectOfResourceConstraint` → **Satisfy** → `OperationalConstraint; ResourceConstraint; ServicePolicy; StrategicConstraint`
- `ResourcePerformer; ServiceSpecification; Standard` → **SuccessorOf** → `ResourcePerformer; ServiceSpecification; Standard`
- `ActualProjectMilestone` → **VersionReleased** → `VersionedElement`
- `VersionOfConfiguration` → **VersionSuccession** → `VersionOfConfiguration`
- `ActualProjectMilestone` → **VersionWithdrawn** → `VersionedElement`

## 🏛️ Architecture

### A1 – Meta-Data Definitions
- `ActualProject; ActualProjectMilestone` → **ArchitectureForProject** → `ArchitecturalDescription`
- `ArchitecturalDescription; DataElement; DocumentReference; InformationElement; ServiceSpecification` → **Classified** → `Classification`
- `Architecture` → **DescribedBy** → `ArchitecturalDescription`
- `Architecture` → **Expresses** → `ArchitecturalDescription`

### A2 – Architecture Products
- `View` → **CompliesViewpoint** → `Viewpoint`
- `ActualEnterprisePhase` → **ConcernForActualEnterprisePhase** → `Concern`
- `View` → **ConcernForView** → `Concern`
- `Viewpoint` → **ConcernForViewpoint** → `Concern`
- `Viewpoint` → **ViewpointToStakeholder** → `Stakeholder`
- `ArchitecturalDescription` → **ViewpointsInArchitecturalDescription** → `Viewpoint`
- `ArchitecturalDescription` → **ViewsInArchitecturalDescription** → `View`

### A3 – Architecture Correspondence
- `ArchitecturalDescription` → **ArchitecturalReference** → `ArchitecturalDescription`

### A6 – Architecture Versions
- `ArchitecturalDescription` → **ArchitecturalSequence** → `ArchitecturalDescription`

### A7 – Architecture Compliance
- `Software; UAFElement` → **SameAs** → `Software; UAFElement`

### A8 – Standards
- `ArchitecturalDescription` → **ArchitecturalSequence** → `ArchitecturalDescription`
- `ActualOrganization` → **RatifiedStandards** → `Standard`

## 🏛️ Requirements

### R2 – Requirement Catalogue
- `RequirementCategory` → **PartOfCatalogue** → `RequirementCatalogue`
- `BWRequirement; RequirementCategory` → **PartOfCategory** → `RequirementCategory`

### R3 – Requirement Dependencies
- `BWRequirement` → **ConflictsWith** → `BWRequirement`
- `BWRequirement` → **IsDuplicateOf** → `BWRequirement`
- `BWRequirement` → **Refines** → `BWRequirement`
- `BWRequirement` → **Replaces** → `BWRequirement`
- `BWRequirement` → **Requires** → `BWRequirement`
- `BWRequirement` → **StemsFrom** → `BWRequirement`

### R7 – Requirement Derivation
- `BWRequirement` → **DerivedFrom** → `UAFElement`
- `BWRequirement` → **ToBeRealizedBy** → `DataElement; Function; Measurement; MeasurementType; Protocol; Protocolstack; ResourcePerformer; ResourcePort; ResourceRole; ServiceFunction; ServiceInterface; ServiceSpecification; ServiceSpecificationRole; Standard`

### R8 – Requirement Fulfilment
- `FulfilmentCriterion` → **Evaluates** → `FitCriterion`
- `DataElement; Function; Measurement; MeasurementType; Protocol; Protocolstack; ResourcePerformer; ResourcePort; ResourceRole; ServiceFunction; ServiceInterface; ServiceSpecification; ServiceSpecificationRole; Standard` → **RealiseRequirement** → `BWRequirement`
