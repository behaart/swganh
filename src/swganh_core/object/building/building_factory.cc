// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE

#include "building_factory.h"

#include "building.h"

#include <cppconn/exception.h>
#include <cppconn/connection.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>
#include <cppconn/prepared_statement.h>
#include <cppconn/sqlstring.h>
#include "swganh/logger.h"

#include "swganh/database/database_manager.h"

using namespace std;
using namespace swganh::object;

BuildingFactory::BuildingFactory(swganh::database::DatabaseManagerInterface* db_manager, swganh::EventDispatcher* event_dispatcher)
	: TangibleFactory(db_manager, event_dispatcher)
{
}
uint32_t BuildingFactory::PersistObject(const shared_ptr<Object>& object)
{
	// Persist Tangible and Base Object First
    return TangibleFactory::PersistObject(object);
}

void BuildingFactory::DeleteObjectFromStorage(const shared_ptr<Object>& object)
{
	ObjectFactory::DeleteObjectFromStorage(object);
}

shared_ptr<Object> BuildingFactory::CreateObjectFromStorage(uint64_t object_id)
{
    return TangibleFactory::CreateObjectFromStorage(object_id);
}

shared_ptr<Object> BuildingFactory::CreateObjectFromTemplate(const string& template_name, bool db_persisted, bool db_initialized)
{
	if(db_persisted || db_initialized)
	{
		//TODO: Have to hit the db to make this
		return make_shared<Building>();
	}
	else
	{
		return make_shared<Building>();
	}
}
