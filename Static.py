from enum import Enum, auto

class EXT( Enum ):
    '''Enumeration of database file extensions'''
    NS = auto( )
    DB = auto( )
    ACCDB = auto( )
    XLS = auto( )
    XLSM = auto( )
    XLSX = auto( )
    MDF = auto( )
    HTML = auto( )
    HTM = auto( )
    XHTML = auto( )
    XML = auto( )
    PNG = auto( )
    JPEG = auto( )
    SVG = auto( )


class BOC( Enum ):
    '''Enumeration of object class codes'''
    NS = 0
    PAYROLL = 10
    FTE = 17
    EXPENSES = 36
    CONTRACTS = 37
    WCF = 38
    GRANTS = 41


class NPM( Enum ):
    '''Enumeration of NPM Codes'''
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    H = 7
    J = 8
    M = 9
    NS = 10


class Source( Enum ):
    '''Enumeration of table names'''
    NS = auto( )
    Actuals = auto( )
    Allocations = auto( )
    ApplicationTables = auto( )
    CarryoverEstimates = auto( )
    CarryoverSurvey = auto( )
    Changes = auto( )
    CongressionalReprogrammings = auto( )
    Deobligations = auto( )
    Defactos = auto( )
    DocumentControlNumbers = auto( )
    HumanResourceOrganizations = auto( )
    Obligations = auto( )
    OperatingPlans = auto( )
    OperatingPlanUpdates = auto( )
    QueryDefinitions = auto( )
    RegionalAuthority = auto( )
    ReimbursableAgreements = auto( )
    ReimbursableFunds = auto( )
    ReimbursableSurvey = auto( )
    Reports = auto( )
    BudgetControls = auto( )
    AppropriationDocuments = auto( )
    BudgetDocuments = auto( )
    Reprogrammings = auto( )
    SiteActivity = auto( )
    SpecialAccounts = auto()
    SiteProjectCodes = auto( )
    StatusOfFunds = auto( )
    Supplementals = auto( )
    Transfers = auto( )
    HeadquartersAuthority = auto( )
    TravelObligations = auto( )
    StatusOfAppropriations = auto( )
    StatusOfJobsActFunding = auto( )
    StatusOfSupplementalFunding = auto( )
    StateGrantObligations = auto( )
    SuperfundSites = auto( )
    PayrollAuthority = auto( )
    PayrollActivity = auto( )
    PayrollCostCodes = auto( )
    TransTypes = auto( )
    PayrollRequests = auto( )
    FullTimeEquivalents = auto( )
    CarryoverRequests = auto( )
    CompassLevels = auto( )
    AdministrativeRequests = auto( )
    OpenCommitments = auto( )
    Expenditures = auto( )
    UnliquidatedObligations = auto( )
    UnobligatedBalances = auto( )
    CongressionalControls = auto( )
    NetAuthority = auto( )
    NetTransfers = auto( )
    NetDeobligations = auto( )
    NetObligations = auto( )
    PRC = auto( )
    '''Reference Models: data tables used to describe 
    elements of the account code structure'''
    Accounts = auto( )
    ActivityCodes = auto( )
    AllowanceHolders = auto( )
    Appropriations = auto( )
    Apportionments = auto( )
    BudgetObjectClasses = auto( )
    BudgetOutlays = auto( )
    BudgetResourceExecution = auto( )
    CostAreas = auto( )
    CPIC = auto( )
    CarryoverOutlays = auto( )
    DataRuleDescriptions = auto( )
    Divisions = auto( )
    Documents = auto( )
    FederalHolidays = auto( )
    FinanceObjectClasses = auto( )
    FiscalYears = auto( )
    FiscalYearsBackUp = auto( )
    Funds = auto( )
    FundCategories = auto( )
    FundSymbols = auto( )
    GrowthRates = auto( )
    Goals = auto( )
    GsPayScale = auto( )
    HeadquartersOffices = auto( )
    Images = auto( )
    Messages = auto( )
    MonthlyOutlays = auto( )
    NationalPrograms = auto( )
    Objectives = auto( )
    Organizations = auto( )
    ObjectClassOutlays = auto( )
    ProgramAreas = auto( )
    ProgramDescriptions = auto( )
    ProgramFinancingSchedule = auto( )
    ProgramProjects = auto( )
    Projects = auto( )
    Providers = auto( )
    PublicLaws = auto( )
    ReferenceTables = auto( )
    RegionalOffices = auto( )
    ResourcePlanningOffices = auto( )
    ResponsibilityCenters = auto( )
    SchemaTypes = auto( )
    SpendingRates = auto( )
    Sources = auto( )
    SubAppropriations = auto( )
    StateOrganizations = auto( )
    WorkCodes = auto( )


class Provider( Enum ):
    '''Enumeration of data providers'''
    SQLite = 0
    SqlServer = 1
    Access = 2
    Excel = 3
    CSV = 4
    NS = 5


class Model( Enum ):
    '''Enumeration of model types'''
    Data = auto( )
    Reference = auto( )


class ParamStyle( Enum ):
    '''Enumeration of paramstyles'''
    format = 1
    number = 2
    pyformat = 3
    name = 4
    qmark = 5
    NS = 6


class SQL( Enum ):
    '''Enumeration of sql commands'''
    SELECT = 0
    SELECTALL = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4
    DROPTABLE = 5
    DROPVIEW = 6
    CREATETABLE = 7
    CREATEVIEW = 8
    ALTERTABLE = 9
    ALTERCOLUMN = 10


class Client( Enum ):
    '''Enumeration of auxiliary applications'''
    NS = auto( )
    SQLite = auto( )
    Access = auto( )
    Excel = auto( )
    Linq = auto( )
    Edge = auto( )
    Chrome = auto( )
    ControlPanel = auto( )
    Calculator = auto( )


class PNG( Enum ):
    '''Enumeration of images'''
    NS = auto( )
    Attachment = auto( )
    Access = auto( )
    Adobe = auto( )
    Authority = auto( )
    Appropriation = auto( )
    Add = auto( )
    BFY = auto( )
    Browse = auto( )
    BOC = auto( )
    Budget = auto( )
    Calculator = auto( )
    ControlPanel = auto( )
    CategoricalGrants = auto( )
    Cancel = auto( )
    Calendar = auto( )
    Chart = auto( )
    CSV = auto( )
    Chrome = auto( )
    Contracts = auto( )
    Database = auto( )
    DatabaseAdd = auto( )
    DatabaseDelete = auto( )
    DatabaseRefresh = auto( )
    DatabaseVerify = auto( )
    DatabaseSql = auto( )
    Datagrid = auto( )
    Delete = auto( )
    EFY = auto( )
    Edge = auto( )
    Edit = auto( )
    Excel = auto( )
    Export = auto( )
    Expenses = auto( )
    Filter = auto( )
    File = auto( )
    FileAdd = auto( )
    FileBrowse = auto( )
    FileCopy = auto( )
    FileEdit = auto( )
    FileVerify = auto( )
    FileTransfer = auto( )
    FileWriter = auto( )
    FileReader = auto( )
    FileDelete = auto( )
    FileSearch = auto( )
    First = auto( )
    Folder = auto( )
    FolderBrowse = auto( )
    FolderCopy = auto( )
    FolderDownload = auto( )
    FolderOpen = auto( )
    FolderCompress = auto( )
    Function = auto( )
    FTE = auto( )
    G0 = auto( )
    Google = auto( )
    Grants = auto( )
    Guidance = auto( )
    Home = auto( )
    Import = auto( )
    Left = auto( )
    Last = auto( )
    LUST = auto( )
    Levels = auto( )
    LogOut = auto( )
    Ledger = auto( )
    Menu = auto( )
    Next = auto( )
    No = auto( )
    OK = auto( )
    Play = auto( )
    Print = auto( )
    Previous = auto( )
    PDF = auto( )
    Recycle = auto( )
    Redo = auto( )
    Right = auto( )
    Remove = auto( )
    Refresh = auto( )
    Row = auto( )
    RowCopy = auto( )
    RowEdit = auto( )
    RowDelete = auto( )
    RowInsert = auto( )
    Recertification = auto( )
    Save = auto( )
    Scan = auto( )
    Sigma = auto( )
    Spreadsheet = auto( )
    Sort = auto( )
    Statistics = auto( )
    Sharepoint = auto( )
    Site = auto( )
    SiteTravel = auto( )
    Text = auto( )
    Table = auto( )
    TableAdd = auto( )
    TableDelete = auto( )
    TableSettings = auto( )
    Travel = auto( )
    TSCA = auto( )
    Undo = auto( )
    WCF = auto( )
    WIFIA = auto( )
    Windows = auto( )
    Word = auto( )
    XML = auto( )
    Yes = auto( )


class ICO( Enum ):
    '''Enumeration of ICO files'''
    NS = auto( )
    Access = auto( )
    Browse = auto( )
    CSV = auto( )
    Database = auto( )
    Error = auto( )
    Excel = auto( )
    Ninja = auto( )
    Notification = auto( )
    PDF = auto( )
    Text = auto( )


class RPIO( Enum ):
    '''Enumeration of Resource Planning and Implementation Offices'''
    NS = 0
    R1 = 1
    R2 = 2
    R3 = 3
    R4 = 4
    R5 = 5
    R6 = 6
    R7 = 7
    R8 = 8
    R9 = 9
    R10 = 10
    OA = 11
    OITA = 13
    OMS = 16
    OCFO = 17
    OCSPP = 20
    OAR = 27
    OW = 30
    OIG = 35
    OGC = 39
    OLEM = 75
    OECA = 77


class ACCDB( Enum ):
    '''Enumeration of access database types used in the application'''
    INTEGER = auto( )
    NUMBER = auto( )
    AUTONUMBER = auto( )
    CURRENCY = auto( )
    DATETIME = auto( )
    HYPERLINK = auto( )
    SHORTTEXT = auto( )
    LONGTEXT = auto( )
    RICHTEXT = auto( )
    ATTACHMENT = auto( )
    CALCULATED = auto( )


class DB( Enum ):
    '''Enumeration of SQLite database types used in the application'''
    REAL = auto( )
    TEXT = auto( )
    INTEGER = auto( )
    BLOB = auto( )


class MDF( Enum ):
    '''Enumeration of SQL Server database types used in the application'''
    BIT = auto( )
    INT = auto( )
    DECIMAL = auto( )
    MONEY = auto( )
    DATE = auto( )
    TIME = auto( )
    DATETIME = auto( )
    FLOAT = auto( )
    CHAR = auto( )
    TEXT = auto( )
    NCHAR = auto( )
    NTEXT = auto( )
    VARCHAR = auto( )
    NVARCHAR = auto( )
    BINARY = auto( )
    VARBINARY = auto( )
    IMAGE = auto( )
    DATETIMEOFFSET = auto( )
